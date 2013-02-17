
import os,cgi,sys,sqlite3,time,csv,pprint,pdb,hashlib,re,traceback
from datetime import date,datetime,timedelta
from itertools import count
from StringIO import StringIO as sio
from os import path
try :
   import json
except :
   import simplejson as json

try :
   os.chdir("./web2py")
   sys.path.append(".")

   import wsgiref.handlers
   import gluon.main

   wsgiref.handlers.CGIHandler().run(gluon.main.wsgibase)

except :
   error = sio()
   traceback.print_exc(file=error)
   print "Content-Type: text/html\n\n"
   print ("<html><head/><body><pre>%s</pre></body></html>" %
     error.getvalue())
   sys.exit(0)
   

#print "Content-Type: text/html\n\n"
#print "<html><head/><body>HI from %s,%s</body></html>" % (
#  sys.version_info, sys.platform)
