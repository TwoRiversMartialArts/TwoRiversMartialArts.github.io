
import re

def fill_price(snip,lbl,value) :
    snip = re.sub(r'__amt__',value,snip)
    snip = re.sub(r'__family__',lbl,snip)
    return snip

def make_anchor(id) :
	return '<span class="trma-inst-anchor" id="%s"></span>' % id

context = {

 '*' : { 'family_price' : fill_price, 
         'make_anchor' : make_anchor }

}
