'''
Static site rendering script.  Takes a directory
of templates, and a directory of content, and renders
all pages.  The content includes both static snippets
and dynamic Python code.  The static snippets can be applied
to any page, while the dynamic content is tagged with the
template name so it applies only to that page.

@author Kendall Bailey
'''
from jinja2 import Environment, PackageLoader, Template
import os, codecs, pprint, traceback, six
from os import path
from six import print_, iteritems

def main() :
    env = Environment(
            loader=PackageLoader('trmaweb', 'templates')
          )
    content = {}
    dynamic = {}
    os.chdir( path.dirname(__file__) )

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

    for fn in os.listdir('templates') :
        try :
            t = env.get_template(fn)
        except :
            print_("FAILED: %s" % fn)
            traceback.print_exc()
            continue
        # combine the static content with the dynamic
        # content specific to this page
        context = {}
        context.update(content)
        context.update( dynamic.get(fn,{}) )
        prev = ''
        while True : # keep rendering until no changes
            page = t.render(context)
            if page == prev :
                break
            prev = page
            t = Template(page)

        with codecs.open(path.join("../../",fn),'w',encoding='utf8') as f :
            f.write(page)

if __name__ == "__main__" :
    main()
