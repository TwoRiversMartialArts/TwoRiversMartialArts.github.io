
import re

def fill_price(snip,lbl,value) :
    snip = re.sub(r'__amt__',value,snip)
    snip = re.sub(r'__family__',lbl,snip)
    return snip

def make_anchor(id) :
	return '<span class="trma-inst-anchor" id="%s"></span>' % id

def paypal_buttons(nm, subsc, month, prices):
    args = dict( ('P%d'%i,v) for i,v in enumerate(prices) )
    args.update( dict(nm=nm, subsc=subsc, month=month) )
    return '''
     <div class="row">
     <!-- Subscribe BUTTON -->
     <div class="col-md-5 paypal-button">
     <h3>Recurring Charge Monthly Class Fee (%(nm)s)</h3>

     <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
     <input type="hidden" name="cmd" value="_s-xclick">
     <input type="hidden" name="hosted_button_id" value="%(subsc)s">
     <table>
     <tr><td><input type="hidden" name="on0" value="Family size">Family size</td></tr><tr><td><select name="os0">
	     <option value="Single">Single : $%(P0).2f USD - monthly</option>
	     <option value="Two family members">Two family members : $%(P1).2f USD - monthly</option>
	     <option value="Three family members">Three family members : $%(P2).2f USD - monthly</option>
	     <option value="Four family members">Four family members : $%(P3).2f USD - monthly</option>
	     <option value="Five family members">Five family members : $%(P4).2f USD - monthly</option>
     </select> </td></tr>
     <tr><td><input type="hidden" name="on1" value="Student name(s)">Student name(s)</td></tr><tr><td><input type="text" name="os1" maxlength="200"></td></tr>
     </table>
     <input type="hidden" name="currency_code" value="USD">
     <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_subscribe_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
     <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
     </form>
     
                                </div>
                              <!-- Class fee BUTTON -->
                              <div class="col-md-4 paypal-button">
                                <h3>One Time Charge Monthly Class Fees (%(nm)s)</h3>
     
     <form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
     <input type="hidden" name="cmd" value="_s-xclick">
     <input type="hidden" name="hosted_button_id" value="%(month)s">
     <table>
     <tr><td><input type="hidden" name="on0" value="Family size">Family size</td></tr><tr><td><select name="os0">
	     <option value="Single">Single $%(P0).2f USD</option>
	     <option value="Two family members">Two family members $%(P1).2f USD</option>
	     <option value="Three family members">Three family members $%(P2).2f USD</option>
	     <option value="Four family members">Four family members $%(P3).2f USD</option>
	     <option value="Five family members">Five family members $%(P4).2f USD</option>
     </select> </td></tr>
     <tr><td><input type="hidden" name="on1" value="Student name(s)">Student name(s)</td></tr><tr><td><input type="text" name="os1" maxlength="200"></td></tr>
     </table>
     <input type="hidden" name="currency_code" value="USD">
     <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
     <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
     </form>
      </div>
       <!-- Uniform BUTTON -->
     <div class="col-md-4 paypal-button">
     <h3>Uniform and patch</h3>
     <form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
      <input type="hidden" name="cmd" value="_s-xclick">
      <input type="hidden" name="hosted_button_id" value="VKEBWAQLXNNUW">
      <table>
      <tr><td><input type="hidden" name="on0" value="Select option">Select option</td></tr><tr><td><select name="os0">
       <option value="Uniform and patch">Uniform and patch $40.00 USD</option>
       <option value="Uniform only">Uniform only $35.00 USD</option>
      </select> </td></tr><tr><td>&nbsp;</td></tr>
      <tr><td><input type="hidden" name="on1" value="Branch and Student name(s)">Branch and Student name(s)</td></tr>
          <tr><td><input value="%(nm)s," type="text" name="os1" size="30" maxlength="200"></td></tr>
      </table>
      <input type="hidden" name="currency_code" value="USD">
      <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
      <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
      </form>
     </div>
     </div>
     <br/><br/>
    ''' % args

# ========================================
context = {
 'location-wdm.html' : {
    'BUTTON_BRANCH' : 'Clive/WDM',
    'PRICE_ARR' : [30, 50, 65, 75, 85],
    'CLS_BUTTON_ID' : '4866A5YJNPECN' ,
    'SUBSC_BUTTON_ID' : 'NUA77T77LT7QG'
 },
 'location-carlisle.html' : {
    'BUTTON_BRANCH' : 'Carlisle',
    'PRICE_ARR' : [25, 45, 60, 70, 80],
    'CLS_BUTTON_ID' :  'M8FHZJN42KY58',
    'SUBSC_BUTTON_ID' : 'ZEGDSVCZ2BPXS'
 },
 'location-hub.html': {
    'BUTTON_BRANCH' : 'Hub',
    'PRICE_ARR' : [30, 50, 65, 75, 85],
    'CLS_BUTTON_ID' :  "K44KYJMJWZKCG",
    'SUBSC_BUTTON_ID' : "CJZACC9XLYE48"
 },
 'location-pleasanthill.html' : {
    'BUTTON_BRANCH' : 'Pleasant Hill',
    'PRICE_ARR' : [25, 45, 60, 70, 80],
    'CLS_BUTTON_ID' :  "PMGR7M2PM9EZA",
    'SUBSC_BUTTON_ID' : "C5HCWK693GC46"
 },
 'location-waukee.html' : {
    'BUTTON_BRANCH' : 'Waukee',
    'PRICE_ARR' : [25, 45, 60, 70, 80],
    'CLS_BUTTON_ID' :  "JMXU3TPC3GKYA",
    'SUBSC_BUTTON_ID' : "KAP6FQCC5LGWQ"
 },
 'location-indianola.html' : {
    'BUTTON_BRANCH' : 'Indianola',
    'PRICE_ARR' : [25, 45, 60, 70, 80],
    'CLS_BUTTON_ID' : "NVPR56ELLRKB2",
    'SUBSC_BUTTON_ID' : "7JGZT8DSW65F8"
 },
 'location-winterset.html' : {
    'BUTTON_BRANCH' : 'Winterset',
    'PRICE_ARR' : [25, 45, 60, 70, 80],
    'CLS_BUTTON_ID' :  "3LJ8LZNCSQ4QQ",
    'SUBSC_BUTTON_ID' : "A7N2MH29AQJZQ"
 },
 '*' : { 'family_price' : fill_price, 
         'make_anchor' : make_anchor,
         'paypal_buttons' : paypal_buttons,
         'EXPLAIN_PPAL_BUTTONS' :
         '''
           <div class="row paypal-code">{{ make_anchor("paybuttons") }}
             <div class="col-md-12">
               <br/>
               <h3><strong>Use these buttons to pay with Paypal or credit/debit card:</strong></h3>
               <br/>
               <p>Select the items you wish to pay for, and on the shopping cart page, you
               can select a quantity for each.  For class fees, The quantity
               value determines the number of months
               you'd like to pay for.  If paying for one session at a time, set the quantity value to
               2.  You can pay for as many months as you like.
               </p><br/><p>Signing up for a subscription requires a
               Paypal account, to manage the subscription, and will charge the same fees
               on a monthly basis.  If you don't have a Paypal account, you can create
               one during the checkout process.</p><br/>
               <p>At any time, you can use the "view cart" button to see your shopping cart:</p><br/>

               {{ VIEW_CART }}

               <br/>
               <br/>
             </div>
            </div>
         ''',
         'VIEW_CART' : 
         '''
         <form target="paypal" action="https://www.paypal.com/cgi-bin/webscr"
         method="post" >
         <input type="hidden" name="cmd" value="_s-xclick">
         <input type="hidden" name="encrypted"
          value="-----BEGIN PKCS7-----MIIG1QYJKoZIhvcNAQcEoIIGxjCCBs'''
          '''ICAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVB'''
          '''AgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQ'''
          '''YXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQ'''
          '''IbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQ'''
          '''AwDQYJKoZIhvcNAQEBBQAEgYArXE7JrbguxqlEf9XXESdRCXysGeU+S'''
          '''BTxTRuKkKTdlOwRbQ0vJ0p9RPLkiEA7pbg5hlCgDOuaf6cRP+DHts03'''
          '''R6OfII4woEikR2kR0xqMkV21aNl2P0UfffBsf1G8aP1YSkZemibIgie'''
          '''pRL0S0xLc7Mnio67pcoizC9fYwSsEUDELMAkGBSsOAwIaBQAwUwYJKo'''
          '''ZIhvcNAQcBMBQGCCqGSIb3DQMHBAgfZYbwJSUdRoAwVcekKluWUTr0V'''
          '''67J/we0bRbcAQfjXQX9gDpjRcLnNM2FZQD4htvmVXTiQ0LHMedmoIID'''
          '''hzCCA4MwggLsoAMCAQICAQAwDQYJKoZIhvcNAQEFBQAwgY4xCzAJBgN'''
          '''VBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVm'''
          '''lldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY'''
          '''2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1y'''
          '''ZUBwYXlwYWwuY29tMB4XDTA0MDIxMzEwMTMxNVoXDTM1MDIxMzEwMTM'''
          '''xNVowgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBx'''
          '''MNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARB'''
          '''gNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJ'''
          '''KoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMIGfMA0GCSqGSIb3DQEBAQU'''
          '''AA4GNADCBiQKBgQDBR07d/ETMS1ycjtkpkvjXZe9k+6CieLuLsPumsJ'''
          '''7QC1odNz3sJiCbs2wC0nLE0uLGaEtXynIgRqIddYCHx88pb5HTXv4SZ'''
          '''euv0Rqq4+axW9PLAAATU8w04qqjaSXgbGLP3NmohqM6bV9kZZwZLR/k'''
          '''lDaQGo1u9uDb9lr4Yn+rBQIDAQABo4HuMIHrMB0GA1UdDgQWBBSWn3y'''
          '''7xm8XvVk/UtcKG+wQ1mSUazCBuwYDVR0jBIGzMIGwgBSWn3y7xm8XvV'''
          '''k/UtcKG+wQ1mSUa6GBlKSBkTCBjjELMAkGA1UEBhMCVVMxCzAJBgNVB'''
          '''AgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQ'''
          '''YXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQ'''
          '''IbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb22CAQ'''
          '''AwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQCBXzpWmoBa5'''
          '''e9fo6ujionW1hUhPkOBakTr3YCDjbYfvJEiv/2P+IobhOGJr85+XHhN'''
          '''0v4gUkEDI8r2/rNk1m0GA8HKddvTjyGw/XqXa+LSTlDYkqI8OwR8GEY'''
          '''j4efEtcRpRYBxV8KxAW93YDWzFGvruKnnLbDAF6VR5w/cCMn5hzGCAZ'''
          '''owggGWAgEBMIGUMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExF'''
          '''jAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJ'''
          '''bmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2F'''
          '''waTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbQIBADAJBgUrDg'''
          '''MCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9'''
          '''w0BCQUxDxcNMjAwNTMwMDI1NTQ0WjAjBgkqhkiG9w0BCQQxFgQUFAZ1'''
          '''bS+zeuAPGFjuCReYM4vuAV8wDQYJKoZIhvcNAQEBBQAEgYC0ADx4nYe'''
          '''o5D71VjMRjwfPlmZNgVtlwSOj54yjPEiedACrEqx24wnCkhJLMr2feN'''
          '''487OGyMKrUqpKbU1f+MH4eKCxF1/e8hSYLzTPUyQDocsHrwjD1dseV1'''
          '''N4ho0tpbfyl+WkQQpsLPivox/BopWMj44bMq24rI2BXp1++dA5TEg=='''
          '''-----END PKCS7-----">
          <input type="image"
          src="https://www.paypalobjects.com/en_US/i/btn/btn_viewcart_LG.gif"
          border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
         <img alt="" border="0"
          src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif"
          width="1" height="1">
         </form>
         ''' 
          }
}

