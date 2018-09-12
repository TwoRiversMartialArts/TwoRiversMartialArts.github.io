'''
Static site rendering script.  Takes a directory
of templates, and a directory of content, and renders
all pages.  The content includes both static snippets
and dynamic Python code.  The static snippets can be applied
to any page, while the dynamic content is tagged with the
template name so it applies only to that page.

@author Kendall Bailey
'''
import sys
from jinja2 import Environment, PackageLoader, Template
import os, codecs, pprint, traceback, six
from os import path
from six import print_, iteritems

sys.path.append(path.abspath( path.join(path.dirname( __file__ ), '..')))

tmpl = 'templates'
s_tmpl = len(tmpl)+1

def main() :
    env = Environment(
            loader=PackageLoader('trmaweb', tmpl)
          )
    content = {}
    dynamic = {}
    os.chdir( path.dirname(__file__) or '.' )

    # read all static and dynamic content
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

    for pth in walk(tmpl) :
        if 'layout' in pth : continue

        try :
            t = env.get_template(pth[s_tmpl:])
        except :
            print_("FAILED: %s" % pth)
            traceback.print_exc()
            continue
        # combine the static content with the dynamic
        # content specific to this page
        fn = path.basename(pth)        
        context = {}
        context.update(content )
        context.update( dynamic.get('*',{}) )
        context.update( dynamic.get(fn,{}) )
        prev = ''
        while True : # keep rendering until no changes
            page = t.render(context)
            if page == prev :
                break
            prev = page
            t = Template(page)

        with codecs.open(path.join("../../",pth[s_tmpl:]),'w',encoding='utf8') as f :
            f.write(page)

def walk(pth) :
    for p,_,fls in os.walk(pth) :
        for f in fls :
            yield path.join(p,f)

if __name__ == "__main__" :
    main()
