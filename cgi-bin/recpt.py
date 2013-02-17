#!/usr/bin/env python

#----------------------------------------------------------------------- 
class Recpt :
   hdrs = ["recpt_no","recpt_date","recpt_branch",
           "recpt_outby","recpt_recvby",
           "recpt_revcount","note"]
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
      res = { 'msg':'SUCCESS','uid':encUID(self.userid) }
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
         if not row['recpt_item'] : continue
         itemid = self._finditemid(row['recpt_item'])
         recptQty = int(row['recpt_qty'])
         if itemid is None: return self.sendJSON({'msg':"Bad item"})        
         self.cur.execute("""insert into recpt_dtl
            (recptid,userid,itemid,qty) values
            (?,?,?,?)""",(rid,self.user,itemid,recptQty))
         incr(recptQtyByItem,itemid,recptQty)
      for row in self.map['recon'] :
         if not row['recon_item'] : continue
         itemid = self._finditemid(row['recon_item'])
         reconQtyRtn = int(row['recon_rqty'] or 0)
         reconQtyPd = int(row['recon_pqty'] or 0)
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
      self.sendJSON({'msg':'Data stored','cnt':str(cnt)})
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
      itemid = self._finditemid(name,1)
      self.cur.execute("""
         select itemid,total from stock_levels
         where itemid = ?
      """,(itemid,))
      row = self.cur.fetchone()
      if not row : return self.sendJSON({ 'count':0 })
      return self.sendJSON({'count':row[1]})      
   #===============
   def stock_store(self):
      if not self.user :
         return self.sendJSON({'msg':"Not logged in"})
      item = self.arg('item')
      if not item :
         return self.sendJSON({'msg':"No item name entered"})
         
      itemid = self._finditemid(self.arg('item'))
      if itemid is None : return self.sendJSON({'msg':"Unrecognized item"})
      
      newcnt = self.arg('setqty')
      if newcnt :
         self.cur.execute("""delete from stock where
            itemid=? and ts = ? and dtl like ?""",
            (itemid,ts(self.arg("stk_date")),"COUNT%%"))
         self.cur.execute("""
           replace into stock (itemid,ts,qty,dtl,userid)
           values (?,?,?,?,?)
           """,(itemid,ts(self.arg('dt')),
              int(newcnt),"COUNT",self.user))
      addcnt = self.arg("addqty")
      if addcnt :
         self.cur.execute("""
            insert into stock (itemid,ts,qty,dtl,userid)
            values (?,?,?,?,?)
           """,(itemid,ts(self.arg('dt')),
              int(addcnt),"CHANGE|"+self.arg('note'),self.user))
      reord = self.arg("reord")
      if reord:
         self.cur.execute("""replace into item_reorder
            (itemid,reorder_level) values (?,?)""",
            (itemid,int(reord)) )
      self.cur.connection.commit()
      return self.sendJSON({'msg':'Data stored'})
      
   #===============
   def search(self) :
      num = self.arg('recpt_no')
      revno = self.arg('recpt_revno')
      self.computeOpen(num)
      if not revno :
         self.cur.execute("""select id,num,branchid,removedby,
                          recvby,ts,createts,rev,status,cnt,note
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
                          A.recvby,A.ts,A.createts,A.rev,A.status,R.cnt,A.note
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
      msg = "Success%s" % (" (note: this receipt is CLOSED)"
                  if hdr[8]=='CLOSED' else '')   
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
   def computeOpen(self,num = None) :
      self.cur.execute("""
         select * from rpt_open_recpts %s
         """ % (num and "where RecptNo = ?" or ""),
          num and (num,) or ())
      rows = {}
      res = []
      desc = self.cur.description
      for row in self.cur:
         rows.setdefault(row[2],[]).append(row)
         
      for num,recs in rows.iteritems() :
         if sum(x[9] for x in recs) == 0 :
            self.cur.execute("update recpt set status = ? where id = ?",
               ("CLOSED",recs[0][0]))
            self.cur.connection.commit()
         else :
            res.extend(recs)
      res.sort(key=lambda x:x[1])
      
      return desc, res
   #===============
   def rptOpen_g(self) :
      col = fgCol
      grd = JS(colModel=[col('Date',w=65),
               col('Receipt#',w=65),
               col('RcvBy',w=90),
               col('RcvEmail',w=80),
               col('Branch',w=130),
               col('item',w=200),col('Qty',w=45),col('Returned'),col('Paid For'),
               col('Remaining'),col('days',w=30)],
               title='Open Receipts')
      return self.sendJSON({'grid':grd.d,'param':fgParam(action="rptOpen")})
   #===============
   def rptOpen(self) :
      desc,rows = self.computeOpen()
      res = [ list(x) for x in rows ]
      self.cur.execute("select name,email from person")
      email = dict([(x[0],x[1]) for x in self.cur])
      print str(email)
      for r in res :
         r[0:2] = [ scrdt(r[1]) ]
         r[3:3] = [ email.get(r[2],'') ]
         r.append( dayspast( r[0] ) )
      return self.sendJSON( fgData(res) )
   #===============
   def rptBranch_g(self) :
      col = fgCol
      grd = JS(colModel=[col('Branch',w=130),col('item',w=200),col('Out')],
               title='Branch inventory report')
      return self.sendJSON({'grid':grd.d,'param':fgParam(action="rptBranch")})
   #===============
   def rptBranch(self) :
      self.cur.execute("""select * from rpt_by_branch""")
      res = {}
      for row in self.cur :
         res.setdefault((row[0],row[1]),[]).append(row)
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
      col = fgCol
      grd = JS(colModel=[col('id'),col('item',w=150),col('counted'),
               col('out'),col('returned'),col('change'),
               col('reorder',w=90),col('total')],
               title='Stock Level')
      return self.sendJSON({'grid':grd.d,'param':fgParam(action="rptStock")})
   #===============
   def rptStock(self):
      sql = "select * from stock_levels order by item"
      self.cur.execute(sql,())
      res = fgData(self.cur)
      return self.sendJSON(res)      
   #===============
   def rptReord_g(self) :
      col = fgCol
      grd = JS(colModel=[col('id'),col('item',w=150),col('current'),
               col('reorder',w=90)],
               title='Stock Below Reorder Level')
      return self.sendJSON({'grid':grd.d,'param':fgParam(action="rptReord")})
   #===============
   def rptReord(self):
      sql = "select * from rpt_item_reorder order by name"
      self.cur.execute(sql,())
      res = fgData(self.cur)
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

   s = smtplib.SMTP('localhost',25)
   s.ehlo()
   #s.login('john.doe@baileyplex.com','pilsung2012')
   email = MIMEMultipart()
   email['From'] = 'trmaweb@tworiversmartialarts.com'
   email['To'] = ", ".join(addr)
   email['Subject'] = subj
   email.attach(MIMEText(msg))
   s.sendmail('trmaweb@tworiversmartialarts.com',addr,email.as_string())
   s.quit()

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
   handler = Recpt(result,form,"web/invapp/inv.db")
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
   

