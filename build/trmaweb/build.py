from jinja2 import Environment, PackageLoader, Template
import os, codecs, pprint, traceback, six, pdb
from os import path
from six import print_, iteritems

def main() :
    env = Environment(
            loader=PackageLoader('trmaweb', 'templates')
          )
    content = {}
    dynamic = {}
    os.chdir( path.dirname(__file__) )

    for fn in os.listdir('content') :
        fnp = path.join('content',fn)
        if not path.isfile(fnp) : continue

        with codecs.open(fnp,encoding='utf8') as f :
           txt = f.read()
        if fn.endswith(".snip") :
           content[fn[:-5]] = txt
        elif fn.endswith(".py") :
           data = {}
           six.exec_(txt,data)
           for tn, ctx in iteritems(data.get('context',{})) :
               dynamic.setdefault(tn,{}).update(ctx)

    for fn in os.listdir('templates') :
        try :
            t = env.get_template(fn)
        except :
            print_("FAILED: %s" % fn)
            traceback.print_exc()
            continue
        context = {}
        context.update(content)
        context.update( dynamic.get(fn,{}) )

        pass1 = t.render(context)
        t = Template(pass1)
        pass2 = t.render(context)

        with codecs.open(path.join("site",fn),'w',encoding='utf8') as f :
            f.write(pass2)

if __name__ == "__main__" :
    main()
