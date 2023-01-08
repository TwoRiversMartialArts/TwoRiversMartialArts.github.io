
def linktofn( prefix ) :
    def lt(x) :
        if 'index.html' in x :
            return '"../index.html"'
        return '"%s%s"' % (prefix,x)
    return lt

def indexlt(x) :
    # if x == '#' : return '"index.html#"'
    if 'index.html' in x : 
        return x
    return linktofn('web/')(x)

context = {

  '*' :          { 'linkto' : linktofn('') },
  # if index is outside folder of other pages, 
  #   set the prefix accordingly
  
  'index.html' : { 'linkto' : indexlt },
  'annualmeeting.html' : { 'linkto' : indexlt },
  'donate.html' : { 'linkto' : indexlt }  
  
}
