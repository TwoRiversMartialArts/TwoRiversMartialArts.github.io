
import re

def fill_price(snip,lbl,value) :
    snip = re.sub(r'__amt__',value,snip)
    snip = re.sub(r'__family__',lbl,snip)
    return snip

def make_anchor(id) :
	return '<span class="trma-inst-anchor" id="%s"></span>' % id

context = {

 '*' : { 'family_price' : fill_price, 
         'make_anchor' : make_anchor,
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
