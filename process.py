#!/usr/bin/env python

import re,sys

def main() :
   with open(sys.argv[1],'r') as f :
      all = f.read()
      all = re.sub(r"(?ms)#(?!&).*?$","",all)
      all = re.sub(r"(?ms)#&","#",all)
      blocks = all.split('@@@')
      spec = [ (x,y) for block in blocks
               for a,b in (block.split("~"),) 
                 for x,y in ((a.strip(),b.strip()),) 
                   if x and y ]
   if len(sys.argv) > 2 :
      with open(sys.argv[2],'r') as f :
         src = f.read()
   else : src = sys.stdin.read()
   for repl in spec :
      #sys.stderr.write("\n---\n%s~%s" % (repl[0],repl[1]))
      src = re.sub(repl[0],repl[1],src,flags=re.M)

   if len(sys.argv) > 3 :
      with open(sys.argv[3],'w') as f :
         f.write(src)
   else : sys.stdout.write(src) 
         

if __name__ == "__main__" :
   main()
