
import re

def fill_price(snip,lbl,value) :
    snip = re.sub(r'__amt__',value,snip)
    snip = re.sub(r'__family__',lbl,snip)
    return snip

context = {

 '*' : { 'family_price' : fill_price }

}
