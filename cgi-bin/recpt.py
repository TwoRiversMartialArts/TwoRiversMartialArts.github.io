#!/usr/bin/env python

#----------------------------------------------------------------------- 
class Recpt :
   hdrs = ["recpt_no","recpt_date","recpt_branch",
           "recpt_outby","recpt_recvby",
           "recpt_revcount","note","recpt_loc",
           "xfer_toggle"]
   recptFields = ["recpt_item","recpt_qty"]
   reconFields = ["recon_item","recon_rqty","recon_pqty","recon_chkn",
                   "recon_paid","recon_pdate","recon_rdate"]
   #===============
   def __init__(self,outp,h,dbfn = "./inv.db") :
      self.outp = outp
      self.h = h
      self.dbfn = dbfn

      self.user, uid = '',self.arg("uid")
      if len(uid) > 25 : self.user = decUID(uid)
      else : self.userid = uid

      # grab all the page data into a data structure
      self.map = { "recpt" : [], "recon": [] }
      for nm in self.map :
         for i in count() :
            rr = dict( (k,self.arg("%s%d"%(k,i))) 
                       for k in getattr(self,nm+'Fields') )
            if rr[nm+'_item'] : self.map[nm].append(rr)
            elif sum( len(v) for v in rr.itervalues() ) == 0 : break
      for h in self.hdrs : self.map[h] = self.arg(h).strip()
      self._cur = None
   #===============
   def getCur(self) :
      if self._cur is None :
         self._cur = sqlite3.connect(self.dbfn).cursor()
      return self._cur
   cur = property(fget = getCur)
   #===============
   def __del__(self) :
      if self._cur :
         con = self.cur.connection
         self._cur.close()
         con.close()
         self._cur = None
   #===============
   def sendJSON(self,obj) :
      if hasattr(self.h,'sendJSON') :
         return self.h.sendJSON(obj)
      else :
         self.outp.write("Content-Type: application/json\n\n")
         json.dump(obj,self.outp)
   #===============
   def arg(self,k,d="") :
      return self.h.getvalue(k,d)         
   #===============
   def log_in(self) :
      hsh = hashpwd( self.arg('pwd') )
      self.cur.execute("select email from user where id=? and pwdhash=?",
                        (self.userid,hsh))
      row = self.cur.fetchone()
      if not row : return self.sendJSON({'msg':'FAILED'})
      self.cur.execute("select name from location order by id")
      locs = [ r[0] for r in self.cur ]
      res = { 'msg':'SUCCESS','uid':encUID(self.userid),'locs':locs }
      if row[0] is None : res['needemail'] = True
      return self.sendJSON(res)
      
   #===============
   def email(self):
      email = self.arg('email').strip()
      exp = re.compile(r"(?i)^[^@]+@[A-Z0-9.-]+\.[A-Z]{2,6}$")
      if not exp.search(email) :
         return self.sendJSON({'msg':'Invalid address'})
      self.cur.execute("update user set email = ? where id = ?",
        (email,self.user))
      self.cur.connection.commit()
      return self.sendJSON({'msg':'SUCCESS'})
   #===============
   def rpemail(self) :
      email = self.arg('email').strip()
      name = self.arg('name').strip()
      exp = re.compile(r"(?i)^[^@]+@[A-Z0-9.-]+\.[A-Z]{2,6}$")
      if email and not exp.search(email) :
         return self.sendJSON({'msg':'Invalid address'})
      self.cur.execute("select 1 from person where name = ?",(name,))
      if self.cur.fetchone() :
         self.cur.execute("update person set email = ?,creatorid=? where name = ?",
            (email,self.user,name))
      else :
         self.cur.execute("insert into person (name,creatorid,email) values (?,?,?)",
            (name,self.user,email))
      self.cur.connection.commit()
      return self.sendJSON({'msg':'SUCCESS'})
   #===============
   def store(self) :
      isxfer = (self.map['xfer_toggle'] == 'T')
      if isxfer : return self.xfer_store()
      rn = self.map['recpt_no']
      if not self.user :
         return self.sendJSON({'msg':"Can't commit unless you are logged in"})
      if not rn :
         return self.sendJSON({'msg':"Can't store receipt with no number"})
      br = self.map["recpt_branch"]
      rm = self.map["recpt_outby"]
      rcv = self.map["recpt_recvby"]
      dt = self.map["recpt_date"]
      notetxt = self.map["note"]
      
      br = self._findbranchid(br)
      
      rev = time.time()
      cts = createts()
      self.cur.execute("""insert into recpt (num,branchid,removedby,
                          recvby,ts,rev,note) 
                          values(?,?,?,?,?,?,?)""",
           (rn,br,rm,rcv,ts(dt),rev,notetxt) )
      rid = self.cur.lastrowid
      recptQtyByItem = {}
      reconQtyByItem = {}
      incr = lambda m,k,v : m.__setitem__(k,m.get(k,0)+v)
      for row in self.map['recpt'] :
         recptQty = int(row['recpt_qty'] or 0)
         if not recptQty : continue
         itemid = self._finditemid(row['recpt_item'])
         if itemid is None: return self.sendJSON({'msg':"Bad item"})        
         self.cur.execute("""insert into recpt_dtl
            (recptid,userid,itemid,qty) values
            (?,?,?,?)""",(rid,self.user,itemid,recptQty))
         incr(recptQtyByItem,itemid,recptQty)
      for row in self.map['recon'] :
         reconQtyRtn = int(row['recon_rqty'] or 0)
         reconQtyPd = int(row['recon_pqty'] or 0)
         if not (reconQtyRtn+reconQtyPd) : continue
         itemid = self._finditemid(row['recon_item'])
         if itemid is None: return self.sendJSON({'msg':"Bad item"})
         incr(reconQtyByItem,itemid,reconQtyRtn+reconQtyPd)
         if reconQtyByItem[itemid] > recptQtyByItem.get(itemid,0) :
             return self.sendJSON({'msg':"FAILED: Can't return/pay for more "
                                   "than was removed.  Nothing stored!"})
         self.cur.execute("""insert into recon_dtl
            (recptid,userid,itemid,rqty,rdate,pqty,paid,
            pdate,chkn) values (?,?,?,?,?,?,?,?,?)""",
            (rid,self.user,itemid,reconQtyRtn,
              ts(row['recon_rdate']),reconQtyPd,
              money(row['recon_paid'].replace("$","")),
              ts(row['recon_pdate']),row['recon_chkn'].strip()))
      self.cur.connection.commit()
      self.cur.execute("""select cnt from recpt_recent_rev 
         where num = ?""",(rn,))
      cnt = self.cur.fetchone()[0]
      return self.sendJSON({'msg':'Receipt stored.  Thank you!','cnt':str(cnt)})
   #===============
   def xfer_store(self) :
      locs = [ self.arg('recpt_x'+x) for x in ('from','to') ]
      if locs[0] == locs[1] :
         return self.sendJSON({'msg':"Locations need to be different"})
      locstr = "%s->%s" % (locs[0],locs[1])
      locids = [ self._getloc(x) for x in locs ]
      dt = self.map["recpt_date"]
      for row in self.map['recpt'] :
         recptQty = int(row['recpt_qty'] or 0)
         if not recptQty : continue
         itemid = self._finditemid(row['recpt_item'])
         if itemid is None: return self.sendJSON({'msg':"Bad item"})        
         self.cur.execute("""insert into stock
            (itemid,qty,dtl,userid,ts,locid) values
            (?,?,?,?,?,?)""",(itemid,-recptQty,
            "XFEROUT|%s"%locstr,self.user,ts(dt),locids[0]))      
         self.cur.execute("""insert into stock
            (itemid,qty,dtl,userid,ts,locid) values
            (?,?,?,?,?,?)""",(itemid,recptQty,
            "XFERIN|%s"%locstr,self.user,ts(dt),locids[1]))
      self.cur.connection.commit()
      return self.sendJSON({'msg':'Transfer stored.  Thank you!','cnt':'0'})
      
   #===============
   def _findbranchid(self,br) :
      self.cur.execute("select id from branch where name = ?",(br,))
      r = self.cur.fetchone()
      if not r : 
         self.cur.execute("""insert into branch (name) values (?)""",
            (br,))
         return self.cur.lastrowid
         self.cur.connection.commit()
      return r[0]
   #===============
   def _finditemid(self,item,canCreate=0) :
      self.cur.execute("select id from item where name =?",
                       (item,))
      r = self.cur.fetchone()
      if (not r) :
         if canCreate :
            self.cur.execute("insert into item (name) values(?)",
               (item,))
            itemid = self.cur.lastrowid
            self.cur.connection.commit()
         else : return None
      else : itemid = r[0]
      return itemid
   #===============
   def _getbranch(self,id) :
      self.cur.execute("select name from branch where id = ?",(id,))
      return self.cur.fetchone()[0]
   #===============
   def _getitem(self,id) :
      self.cur.execute("select name from item where id = ?",(id,))
      return self.cur.fetchone()[0]
   #===============
   def _getloc(self,key) :
      if isinstance(key,(int,long)) :
         self.cur.execute("select name from location where id = ?",(key,))
      else : 
         self.cur.execute("select id from location where name = ?",(key,))
      row = self.cur.fetchone()
      if not row : print "No loc %s" % str(key)
      return row[0]
   #===============
   def _getnextNUM(self) :
      self.cur.execute("select distinct num from recpt")
      nums = [ int(x[0]) for x in self.cur ]
      nums.sort()
      return nums and (nums[-1]+1) or 1
   #===============
   def nextRecptNum(self) :
      return self.sendJSON({ 'num':str(self._getnextNUM()) })    
   #===============
   def stock_search(self) :
      name = self.arg("item")
      locid = self._getloc(self.arg('loc'))
      itemid = self._finditemid(name,1)
      self.cur.execute("""
         select itemid,total,cost,price from 
           stock_levels A join item B on A.itemid=B.id
         where itemid = ? and locid = ?
      """,(itemid,locid))
      row = self.cur.fetchone()
      if not row : return self.sendJSON({ 'count':0 })
      res = {'count':row[1]}
      if row[2] : res['cost'] = "$%.2f"%row[2]
      if row[3] : res['price'] = "$%.2f"%row[3]
      return self.sendJSON(res)      
   #===============
   def stock_store(self):
      if not self.user :
         return self.sendJSON({'msg':"Not logged in"})
      item = self.arg('item')
      locid = self._getloc(self.arg('loc'))
      if not item :
         return self.sendJSON({'msg':"No item name entered"})
         
      itemid = self._finditemid(self.arg('item'))
      if itemid is None : return self.sendJSON({'msg':"Unrecognized item"})
     
      for attr in ('cost','price') :
         v = self.arg(attr)
         if v :
            v = float(re.sub(r"\s|\$","",v))
            self.cur.execute("update item set %s=? where id =?"%attr,
                             (v,itemid))
            self.cur.connection.commit()
      
      newcnt = self.arg('setqty')
      if newcnt :
         self.cur.execute("""delete from stock where
            itemid=? and ts = ? and dtl like ? and locid = ?""",
            (itemid,ts(self.arg("dt")),"COUNT%",locid))
         self.cur.execute("""
           replace into stock (itemid,ts,qty,dtl,userid,locid)
           values (?,?,?,?,?,?)
           """,(itemid,ts(self.arg('dt')),
              int(newcnt),"COUNT",self.user,locid))
      addcnt = self.arg("addqty")
      if addcnt :
         self.cur.execute("""
            insert into stock (itemid,ts,qty,dtl,userid,locid)
            values (?,?,?,?,?,?)
           """,(itemid,ts(self.arg('dt')),
              int(addcnt),"CHANGE|"+self.arg('note'),self.user,locid))
      reord = self.arg("reord")
      if reord:
         self.cur.execute("""replace into item_reorder
            (itemid,reorder_level,locid) values (?,?,?)""",
            (itemid,int(reord),locid) )
      self.cur.connection.commit()
      return self.sendJSON({'msg':'Data stored. Thank you!'})
      
   #===============
   def search(self) :
      num = self.arg('recpt_no')
      revno = self.arg('recpt_revno')
      _,_,owe = self.computeOpen(num=num)
      if not revno :
         self.cur.execute("""select id,num,branchid,removedby,
                          recvby,ts,createts,rev,status,cnt,note,
                          locid
                          from recpt_recent A
                          where num = ?""",(num,))
      else :
         lim = int(revno)
         self.cur.execute("""select max(rev) from
                             (select rev from recpt where
                               num = ? order by rev asc
                               limit(%d))""" % lim,(num,))
         rev = self.cur.fetchone()
         if rev :
            self.cur.execute("""select A.id,A.num,A.branchid,A.removedby,
                          A.recvby,A.ts,A.createts,A.rev,A.status,R.cnt,A.note,
                          A.locid
                          from recpt A join recpt_recent R
                               on A.num = R.num
                          where A.num = ? and A.rev = ?""",(num,rev[0]))
      hdr = self.cur.fetchone()
      
      if not hdr :
         return self.sendJSON({'msg':'Not Found'})
      self.cur.execute("""select itemid,qty from recpt_dtl
                          where recptid = ?""",(hdr[0],))
      rcptdtl = self.cur.fetchall()
      self.cur.execute("""select itemid,rqty,rdate,pqty,paid,
                          pdate,rdate,chkn from recon_dtl where recptid = ?
                          order by pdate,rdate""",
                          (hdr[0],))
      recondtl = self.cur.fetchall()
      
      result = {}
      result["recpt_no"] = num
      result["recpt_date"] = scrdt(hdr[5])
      result["recpt_branch"] = self._getbranch(hdr[2])
      result["recpt_outby"] = hdr[3]
      result["recpt_recvby"] = hdr[4]
      result["recpt_revcount"] = str(hdr[9])
      result["recpt_revno"] = str(revno or hdr[9])
      result["recpt_loc"] = self._getloc(hdr[11])
      result["note"] = hdr[10] or ''
      
      for i,row in enumerate(rcptdtl) :
         result["recpt_item%d"%i] = self._getitem(row[0])
         result["recpt_qty%d"%i] = scrt(row[1])
      for i,row in enumerate(recondtl) :
         result["recon_item%d"%i] = self._getitem(row[0])
         result["recon_rqty%d"%i] = scrt(row[1])
         result["recon_pqty%d"%i] = scrt(row[3])
         result["recon_paid%d"%i] = scrm(row[4])
         result["recon_pdate%d"%i] = scrdt(row[5])
         result["recon_rdate%d"%i] = scrdt(row[6])
         result["recon_chkn%d"%i] = scrt(row[7])
      msg = "Success, owed item count = %d" % owe   
      return self.sendJSON({'data':result,'msg':msg})
   #===============
   def suggbranch(self) :
      q = self.arg('query')
      self.cur.execute("""select name from branch
         where name like ? 
         order by name limit 100""",
         ("%s%%" % q,) )
      res = {'query':q,
         'suggestions':[ r[0] for r in self.cur ],
         'data' : [] }
      return self.sendJSON(res)
   #===============
   def suggitem(self) :
      q = self.arg('query')
      self.cur.execute("""select name from item
         where name like ?
         order by name limit 100""",
         ("%%%s%%" % q,))
      res = {'query':q,
         'suggestions':[ r[0] for r in self.cur ],
         'data' : [] }
      return self.sendJSON(res)
         
   #===============
   def suggperson(self) :
      q = self.arg('query')
      lk = "%%%s%%" % q
      self.cur.execute("""select name from
         all_names where name like ?
         order by name limit 100""",
         (lk,))
      res = {'query':q,
         'suggestions':[ r[0] for r in self.cur ],
         'data' : [] }
      return self.sendJSON(res)
   #===============
   def computeOpen(self,db=0,num = None) :
      rloc = self.arg('recpt_loc')
      locs = self.arg('locs')
      locs = rloc and [rloc] or (locs and locs.split(",") or []) 
      where = []
      args = ()
      if locs: 
         where.append('( A.name in (%s) )' % ','.join('?'*len(locs))) 
         args += tuple(locs)
      if num :
         where.append('RecptNo = ?')
         args += (num,)
      if db :
         where.append("Date>=?")
         args += (daysback_cutoff(db),)
      elif not num :
         where.append("Remaining>?")
         args += (0,)
  
      self.cur.execute("""
         select A.name,B.*,coalesce(C.userid,'') 
            from 
            location A join rpt_open_recpts B
            on A.id = B.locid
            left outer join (
              select A.id recptid, min(B.userid) userid
              from recpt_recent A join recpt_dtl B on A.id = B.recptid
              group by A.id) C on B.id = C.recptid
            where %s
         """ % " and ".join(where),args) 
      desc = self.cur.description
      res = self.cur.fetchall()
      tot = res and sum([x[11] for x in res]) or 0 
      res.sort(key=lambda x:x[3])
      
      return desc, res, tot
   #===============
   def rptOpen_g(self) :
      locs = self.arg('locs')
      days = self.arg('days')
      col = fgCol
      grd = JS(colModel=[col('LOC',w=20),
               col('Date',w=65),
               col('Receipt#',w=65),
               col('RcvBy',w=90),
               col('RcvEmail',w=80),
               col('Branch',w=80),
               col('item',w=200),col('Qty',w=45),col('Returned'),col('Paid For'),
               col('Remaining'),col('days',w=30),
               col('entered',w=45)],
               title='Open Receipts')
      return self.sendJSON({'grid':grd.d,
              'param':fgParam(action="rptOpen",locs=locs,days=days)})
   #===============
   def rptOpen(self) :
      days = self.arg('days')
      args = (days and dict(db=int(days)) or {})
      desc,rows,_ = self.computeOpen(**args)
      res = [ list(x) for x in rows ]
      self.cur.execute("select name,email from person")
      email = dict([(x[0],x[1]) for x in self.cur])
      for r in res :
         r[:4] = [ r[0],scrdt(r[3]) ]
         r[4:4] = [ email.get(r[3],'') ]
         r[-1:-1] = [ dayspast( r[1] ) ]
      return self.sendJSON( fgData(res) )
   #===============
   def rptBranch_g(self) :
      locs = self.arg('locs')
      col = fgCol
      grd = JS(colModel=[col('Branch',w=130),col('item',w=200),col('Out')],
               title='Branch inventory report')
      return self.sendJSON({'grid':grd.d,
                  'param':fgParam(action="rptBranch",locs=locs)})
   #===============
   def rptBranch(self) :
      locs = self.arg('locs').split(",")
      self.cur.execute("""select A.name,B.* 
        from location A join rpt_by_branch B on A.id = B.locid
        where A.name in (%s) and Owe > 0""" % (','.join('?'*len(locs)),),
        tuple( self.arg('locs').split(",") ) )
      res = {}
      for row in self.cur :
         drow = row[2:]
         res.setdefault((drow[0],drow[1]),[]).append(drow)
      res = fgData( (key[0],key[1],sum(x[2] for x in res[key]))
                     for key in sorted(res.keys()) )
      return self.sendJSON(res)
   #===============
   def _rptSQL(self,sql,args=()):
      sql = sql.strip()
      rpt = sio()
      try : 
         if sql.endswith("commit") and self.user == 'kendall':
            sql = sql[:-6]
            rpt.write("%s\n\n" % sql)
            self.cur.execute(sql,args)
            self.cur.connection.commit()
            rpt.write("Success\n")
         else :
            self.cur.execute(sql,args)
            wr = csv.writer(rpt,lineterminator="\n")
            wr.writerow([x[0] for x in self.cur.description])      
            wr.writerows(self.cur.fetchall())
      except :
         import traceback
         traceback.print_exc(file = rpt)
      return self.sendJSON( {'txt' : rpt.getvalue() } )
   #===============
   def rptSQL(self):
      return self._rptSQL(self.arg('sql'))
            
   #===============
   def rptStock_g(self) :
      locs = self.arg('locs')
      col = fgCol
      grd = JS(colModel=[
               col('id'),col('item',w=150),
               col('cost'),col('price'),
               col('counted'),
               col('out'),col('returned'),col('change'),
               col('reorder',w=90),col('total')],
               title='Stock Level')
      return self.sendJSON({'grid':grd.d,
                  'param':fgParam(action="rptStock",locs=locs)})
   #===============
   def rptStock(self):
      locs = self.arg("locs").split(",")
      locids = [ self._getloc(x) for x in locs ] 
      
      sql = """select itemid,item,cost,price,
                      sum(counted),sum(out),sum(returned),
                      sum(change),sum(reord),sum(total) 
               from stock_levels A join item B
                  on A.itemid = B.id
               where locid in (%s)
               group by item,itemid
               order by item,itemid""" % ','.join('?'*len(locids))
      self.cur.execute(sql,tuple(locids))
      rows = [ list(x) for x in self.cur ]
      res = fgData(rows)
      return self.sendJSON(res)      
   #===============
   def rptTx_g(self) :
      locs = self.arg('locs')
      days = self.arg('days')
      col = fgCol
      grd = JS(colModel=[col('Date',w=90),
               col('Locs',w=115),col('id',w=65),col('item',w=160),
               col('Qty',w=65,a=1)],
               title='Stock transfers')
      return self.sendJSON({'grid':grd.d,
                  'param':fgParam(action="rptTx",locs=locs,days=days)})
   #===============
   def rptTx(self) :
      locs = self.arg('locs').split(",")
      locids = [ self._getloc(x) for x in locs ] 
      days = self.arg('days')
      sql = """select ts,dtl,itemid,name,qty
               from transfers where ts > ?
               and locid in (%s)
               order by ts desc""" % ','.join('?'*len(locids))
      self.cur.execute(sql,(daysback_cutoff(int(days)),)+tuple(locids))
      rows = [ list(x) for x in self.cur ]
      for r in rows : r[0] = scrdt(r[0])
      return self.sendJSON(fgData(rows))
      
   #===============
   def rptReord_g(self) :
      locs = self.arg('locs')
      col = fgCol
      grd = JS(colModel=[col('LOC',w=20),
               col('id'),col('item',w=150),col('current'),
               col('reorder',w=90)],
               title='Stock Below Reorder Level')
      return self.sendJSON({'grid':grd.d,
                  'param':fgParam(action="rptReord",locs=locs)})
   #===============
   def rptReord(self):
      rows = []
      for i in self.arg('locs').split(',') :
         locid = self._getloc(i)
         sql = """select * from rpt_item_reorder
            where locid = ? order by name"""
         self.cur.execute(sql,(locid,))
         
         rs = [list(x) for x in self.cur]
         for r in rs :
            r[0] = i
         rows.extend(rs)
      res = fgData(rows)
      return self.sendJSON(res)
   #===============
   def adduser(self):
      if not self.user : return self.sendJSON({'msg':'Not logged in'})
      newid,newpass = self.arg('newid'),self.arg('pass')
      if newid == self.user :
         self.cur.execute("update user set pwdhash = ? where id = ?",
            (hashpwd(newpass),self.user))
         self.cur.connection.commit()
         return self.sendJSON({'msg':'Your password has been changed'})
      self.cur.execute("select 1 from user where id = ?",(newid,))
      if self.cur.fetchone() and self.user != 'kendall' :
         return self.sendJSON({'msg':'User already exists, password not changed'})
      
      self.cur.execute("""replace into user (id,name,pwdhash,creatorid)
         values (?,?,?,?)""",(newid,'',hashpwd(newpass),self.user))
      self.cur.connection.commit()
      return self.sendJSON({'msg':'User created/updated'})
   #===============
   def beltpull(self) :
      if not self.user :
         return self.sendJSON({'msg':"Not logged in"})

      nms = self.arg("names").split(",")
      ttl = 0
      for n in nms :
         amt = int(self.arg(n) or 0)
         if not amt : continue
         ttl += amt
         np = n.split("_")[1:]
         item = "Belt #%s %s" % (np[1],np[0].replace("0"," "))
         itemid = self._finditemid(item)
         if itemid is None : 
            return self.sendJSON({'msg':"Unrecognized item: %s" % item})
         self.cur.execute("""
            insert into stock (itemid,ts,qty,dtl,userid)
            values (?,?,?,?,?)
           """,(itemid,ts(self.arg('dt')),
              -amt,"CHANGE|beltpull",self.user))
      self.cur.connection.commit()
      return self.sendJSON({'msg':"Success, %d belts pulled" % ttl})
      
   #===============
   def beltdlg(self) :
      html, nms = beltHTML()
      self.sendJSON({'html':str(html),'names':nms})
      
   #===============
   def contact_msg(self) :
      try :
         wdm = 'wdm@tworiversmartialarts.com'
         toaddr = [ x.strip() for x in self.arg('to').split(",") ]
         sender = self.arg('name').strip()
         emailNotice(
            toaddr,
            "from: %s (%s)\nphone: %s\n\n%s\n" 
              % (sender,self.arg('email'),self.arg('phone'),
                 self.arg('msg')),
             "TRMA Website contact form: %s" % self.arg('subj'))
         if (wdm not in toaddr) or (sender == 'kendall') : 
            emailNotice( [wdm],
               "to: %s\nfrom: %s (%s)\nphone: %s\n\n%s\n" 
                 % (str(toaddr),sender,
                    self.arg('email'),self.arg('phone'),
                    self.arg('msg')),
                "TRMA Website contact form: %s" % self.arg('subj'))
         res = self.sendJSON({'msg':'Message sent. Thank you '
                                    'for your interest in TRMA'})
         return res 
      except :
         import traceback
         error = sio()
         traceback.print_exc(file=error)
         self.sendJSON({'msg':
          ('There was a problem, please use an email program to send a '
          'message to one of the addresses listed above')})
   #===============
   def backupDB(self) :
      try :
         bkupDB(self.dbfn)
      except :
         import traceback
         err = sio()
         traceback.print_exc(file=err)
         return self.sendJSON({'msg':err.getvalue()})
      return self.sendJSON({'msg':'Success'})
           
#----------------------------------------------------------------------- 
def beltHTML() :
   "Create an HTML table for a belt pull"
   colors = "Yellow,Orange,Green,Blue,Brown,Temp0Black".split(",")
   sizes = [ ("#%d"%i) for i in range(0,9) ]
   tbl = Tag('table',i='belt_pull_tbl')
   hdr = tbl.add(Tag('tr',ch=[Tag('td')]))
   for sz in sizes: hdr.add(Tag('td',ch=[Tag('span',c='belt_sz_hdr',t=sz)])) 
   inpnames = []
   for col in colors :
      row = tbl.add(Tag('tr',ch=[Tag('td',ch=[Tag('span',c='belt_col_hdr',
                        t=col.replace("0"," "))])]))
      for sz in sizes :
         nm = "blt_%s_%s"%(col,sz[-1])
         inpnames.append(nm)
         inp = Tag('input',size="3",i=nm,c="blt_num_inp") 
         row.add(Tag('td',ch=[inp]))
   return tbl,inpnames
 
#----------------------------------------------------------------------- 
class Tag :
   def __init__(self,tag,t='',**kw) :
      self.tag,self.t = tag,t
      self.ch = kw.get('ch',[])
      self.attr = { 'id' : kw.get('i'), 
                    'class': kw.get('c') }
      self.attr.update(dict([(k,v) for k,v in kw.items()
                 if k not in ('i','c','ch')]))

   def add(self,ch) : 
      self.ch.append(ch)
      return ch
   def attr(self,nm,val) :
      self.attr[nm] = val
   def __str__(self) :
      return "<%s%s>%s%s</%s>\n" % (self.tag,
        "".join([ (""" %s="%s" """% (k,v)) 
                 for k,v in self.attr.iteritems() if k if v]),
        self.t or '',
        "\n".join([ str(x) for x in self.ch]),
        self.tag)
#----------------------------------------------------------------------- 
# utility functions
def encUID(uid) :
   import random, base64
   pad = int(random.random()*5)+4
   pv = lambda n : ''.join([ chr(ord('a')+int(random.random()*26)) for i in range(n) ]) 
   return base64.b64encode( "%s%s%s*%s" % (str(pad),pv(pad*5),uid,pv(pad)) )
def decUID(uid) :
   import base64
   if not uid : return uid
   v = base64.b64decode(uid)
   ps = int(v[0])
   if v[-ps-1] != '*' :
      raise ValueError('bad user') 
   return v[(1+5*ps):-(ps+1)]

def scrt(v) : # displayable-text
   return v and str(v) or ''
def scrm(v) : # displayable-money
   return v and ("$%0.2f" % v) or ''
def scrdt(v) : # displayable-date
   if not v : return ''
   ymd = v.split("/")
   return "%s/%s/%s" % (ymd[1],ymd[2],ymd[0])
def money(v) : # parse an input money value
   if not v : return v
   return float( v.replace("$","") )  
def createts() : # current date formatted for db storage
   return datetime.today().strftime("%Y/%m/%d")
def daysback_cutoff(n) :
   back = datetime.today() - timedelta(days=n)
   return back.strftime("%Y/%m/%d")
def ts(v) : # parse date and convert to format for db storage
   if not v: return ''
   dt = [ int(x) for x in v.split("/") ]
   dt = datetime( dt[2],dt[0],dt[1],0,0,0)
   return dt.strftime("%Y/%m/%d")
def dayspast(d) :
   mm,dd,yy = d.split("/")
   ddd = (int(yy),int(mm),int(dd),12,0,0)
   delta = datetime.today() - datetime(*ddd)
   return max(0,delta.days)
def hashpwd(pwd) :
   md5 = hashlib.md5()
   md5.update( "%s::pilsung" % pwd )
   return "md5:%s" % md5.hexdigest()   

def fgCol(d,n='',w=50,a=0): 
   return JS(display=d,name=n or d,
              width=w,sortable=False,align=(a and 'right' or 'left')).d
def fgParam(**kw) :
   return [ {'name':k, 'value':v} for k,v in kw.iteritems() ]

def fgData(rows) :
   rows = list(rows)
   return JS(page=1,total=len(rows),rows=
             [ {'id':str(i),'cell':list(r)} for i,r in enumerate(rows) ]).d
   
#----------------------------------------------------------------------- 
class JS :
   "Helps build a dict for serialization to JSON format"
   def __init__(self,**kw) : self.d = {}; self.add(**kw)
   def add(self,**kw) : 
      for k,v in kw.iteritems() :
         if isinstance(v,JS) : self.d[k] = v.d
         else : self.d[k] = v
      return self
#----------------------------------------------------------------------- 
def emailNotice(addr,msg,subj) :
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText
   import smtplib

   #s = smtplib.SMTP('smtp.gmail.com',587)
   s = smtplib.SMTP('localhost',25)
   s.ehlo()
   #s.starttls()
   #s.ehlo()
   #smtpuser = 'john.doe@baileyplex.com'
   smtpuser = 'trmaweb@tworiversmartialarts.com'
   s.login(smtpuser,'trmapilsung!')
   email = MIMEMultipart()
   email['From'] = smtpuser
   email['To'] = ", ".join(addr)
   email['Subject'] = subj
   email.attach(MIMEText(msg))
   s.sendmail(smtpuser,addr,email.as_string())
   s.close()

#----------------------------------------------------------------------- 
def bkupDB(fn) :
   import smtplib,imaplib
   # For guessing MIME type based on file name extension
   import mimetypes
   from email import encoders
   from email.message import Message
   from email.mime.base import MIMEBase
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText
   uid,pwd = 'john.doe@baileyplex.com','pilsung2012'
   fp = open(fn, 'rb')
   msg = MIMEBase('application','octet-stream')
   msg.set_payload(fp.read())
   fp.close()
   # Encode the payload using Base64
   encoders.encode_base64(msg)
   # Set the filename parameter
   msg.add_header('Content-Disposition', 'attachment', filename=fn)
   msg['Subject'] = 'Inventory Backup'
   msg['From'] = 'trmaweb@tworiversmartialarts.com'
   msg['To'] = uid
   imap = imaplib.IMAP4_SSL('imap.gmail.com')
   imap.login(uid,pwd)
   imap.append("Inbox",None,None,msg.as_string())
   #imap.close()
   #imap.logout()
#----------------------------------------------------------------------- 
# doAction is the entry point for the custom web server
#----------------------------------------------------------------------- 
def doAction(http) :
   action = http.arg("action")
   if not action : return
   print action
   strm = sio()
   R = Recpt(strm,http)
   try :
      return getattr(R,action)()
   except :
      import traceback
      traceback.print_exc()

#----------------------------------------------------------------------- 
# Try to run as a CGI program
#----------------------------------------------------------------------- 
def main() :
   form = cgi.FieldStorage()
   action = form.getvalue('action')
   if not action : return
   
   result = sio()
   handler = Recpt(result,form,"../httpdocs/web/invapp/inv.db")
   try :
      getattr(handler,action)()
   except :
      import traceback
      error = sio()
      traceback.print_exc(file=error)
      handler.outp = sio()
      handler.sendJSON( {'msg' : error.getvalue()} )
      
   result = handler.outp.getvalue()
   if result : print result

try :
   import cgi,sys,sqlite3,time,csv,pprint,pdb,hashlib,re
   from datetime import date,datetime,timedelta
   from itertools import count
   from StringIO import StringIO as sio
   try :
      import json
   except :
      import simplejson as json
   
   main()
except :
   import sys,traceback
   print "Content-Type: text/html"     # HTML is following
   print                               # blank line, end of headers

   print "<html><head/><body><TITLE>CGI script output</TITLE>"
   print "<H1>Error</H1><br/>"
   print "%s</body></html>" % traceback.print_exc(file = sys.stdout)
   

