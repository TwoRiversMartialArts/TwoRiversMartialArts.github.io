

def linktofn( prefix ) :
	def lt(x) :
		return '"%s%s"' % (prefix,x)
	return lt

context = {

  '*' :          { 'linkto' : linktofn('') },
  # if index is outside folder of other pages, 
  #   set the prefix accordingly
  'index.html' : { 'linkto' : linktofn('') }  
  
}