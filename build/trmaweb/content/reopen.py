
def reopen_block(s):
    pre = '''
    <div class="row"
     style="ackground-color: #d4edda; line-height: 1.6; font-size: 18px; font-weight: bold;">
     <div style="background-color: #d4edda; border: 3px solid black;  border-radius: 23px; margin:8px; margin-bottom:20px">
    <div style="margin:12px">'''

    post = '''
       </div>
       </div>
       <br/><br/>
       </div>'''
    return pre + s + post

CLOSED_TXT='''<p>
Two Rivers has suspended in-person classes through
January 3rd.  Online classes will continue, and 
promotion testing can be arranged either online or
in-person in small groups (1-3 students).
Please <a href="https://forms.gle/Q19aRBkkKCXEE2jZ6">
fill out this form</a> to register interest in
additional belt-level instruction sessions. These
can help you get ready for testing.</p>
'''
CLOSED_= {
        'RE_OPEN' : reopen_block(CLOSED_TXT),
        'RE_OPEN_SCHED' : reopen_block('''
        In-person classes are suspened.  Online zoom
        classes are still being offered.
        <a href="contact.html">Contact us</a>
        for details on how to connect to online classes.
        ''')
    }
context = {
'locations-trma.html' : CLOSED_,
'location-carlisle.html' : CLOSED_,
'location-hub.html' : CLOSED_,
'location-indianola.html' : CLOSED_,
'location-pleasanthill.html' : CLOSED_,
'location-waukee.html' : CLOSED_,
'location-wdm.html' : CLOSED_,
'location-winterset.html' : CLOSED_,
}
