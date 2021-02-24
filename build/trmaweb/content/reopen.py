
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
January 18th.  Online classes will continue, and 
promotion testing can be arranged either online or
in-person in small groups (1-3 students).
Please <a href="https://forms.gle/Q19aRBkkKCXEE2jZ6">
fill out this form</a> to register interest in
additional online belt-level instruction sessions. These
can help you get ready for testing.
In person classes
may resume starting as early as January 19th. Class size will be limited
and face masks required. Information on 
class times and sign-up procedure will be
posted on each branch page soon.</p>
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
 'locations-trma.html' :
    {
        'RE_OPEN' : reopen_block('''
        Each branch page will include
        details of available in-person classes at the top of the page.
        '''),
        'RE_OPEN_SCHED' : reopen_block('''
        Please visit the individual branch pages for
        accurate information regarding class schedules
        amid the COVID-19
        pandemic.  Each page will have a notice like
        this one at the top of the page.
        ''')
    },
 'location-carlisle.html' : {
    'RE_OPEN': reopen_block('''
    Good news. The Carlisle branch is open for classes again. The first class
    back was held Monday, Feb. 22nd. It was a good class with reviewing what
    we have learned. As long as the 7 day average stays below 10% we will
    continue to hold classes.<br/><br/>
    Hope to see you there.
       '''),
    'RE_OPEN_SCHED': reopen_block('') 
 },
'location-hub.html' : {
    'RE_OPEN_SCHED': reopen_block(''),
    'RE_OPEN': reopen_block('''
    <p>
    The Hub location is holding in-person classes. Please follow
    <a href="https://www.signupgenius.com/go/904054ba4a629a0ff2-hub1">
    this link for February signups</a> and
    <a href="https://www.signupgenius.com/go/904054ba4a629a0ff2-hub2">
    this link for March</a>.
    </p><br/>
    <p>
    In person classes will look different. 
    </p>
    <div style="margin-top:6px; margin-left:23px; margin-bottom:10px">
    <ul>
      <li>Class sizes will be restricted to 10 students for the time being
      in order to maintain social distancing.  </li>
      <li>A link to a class sign up sheet will be available (see above).</li>
      <li>Students must sign up for each class they want to attend class
      at the dojang.  This is to help us avoid turning people away at the door.
      </li>
      <li>If at all possible, students should arrive in their dobok. </li>
      <li>Students should bring their own bottle of water.
      The water fountain at the dojang will be off limits for now.</li>
      <li>Face masks, bandanas, or other alternative face coverings
      will be required.</li>
      <li>Because face masks will be required,
      classes will be more technique based and less cardio based.</li>
      <li>Students are strongly encouraged to attend online classes
      for the cardio component.</li>
      <li>New class time for Friday Brown and Black belt class will be from
          6-7pm.</li>
      <li>No spectators will be allowed at this time.</li>
    </ul>
    </div>
    <p>
    Cleaning will be performed between classes and after class.
    </p><br/>
    <p>
    The class schedule and teaching schedule may be adjusted if
    needed depending upon interest.
    </p><br/>
    <p>
    Students are encouraged to take online classes.
    </p><br/>
    <p>
     Curriculum:
     <div style="margin-left:23px; margin-top:6px">
     <ul>
      <li>Kicking</li>
      <li>Punching</li>
      <li>Basic/advanced  movements modified for social distance</li>
      <li>Forms</li>
      <li>Shadow one steps</li>
      <li>shadow Self-defense</li>
      <li>Shadow sparring</li>
      <li>Other</li>
    <ul>
    </div>
    ''')
    },
'location-indianola.html' : {
    'RE_OPEN': reopen_block('''
        We have been monitoring the 14-day and 7-day positivity rates in Warren county.
        As of February 12th, the 14-day positivity rate had dropped below 10%. This means:
        <div style="font-weight:bold; padding-left: 25px">
        <ul>
        <li>We will re-open for in-person classes on Monday, February 15th </li>
        <li>Regular, in-person classes will follow every Monday and Thursday evening-
          <ul><li>White Belts from 6-7 pm</li>
              <li>Colored Belts from 7-8 pm</li>
          </ul></li>
        <li>We will follow Covid protocols for masks and social distancing.
            Enhanced cleaning procedures will be followed each class. </li>
        </ul>
        </div>
        We will remain open for in-person classes as long as the 7-day positivity
        rate for Warren county remains at or below 10%. If that rate goes above 10%,
        we will close again. If you have any questions, contact the branch instructor.
      '''),
    'RE_OPEN_SCHED': reopen_block('') 
    },
'location-pleasanthill.html' : {
    'RE_OPEN': reopen_block('''
         TRMA had a board meeting to discuss reopening in person classes. Certain
         branches will reopen Tuesday January 19th. Pleasant Hill has been training
         at the Carlisle location and Carlisle unfortunately will
         still be closed until Fed 1st due to the high numbers in Warren County
         at which time we will re-evaluate opening. In the meantime Zoom classes
         are still available and you can signup online for in person classes at the Hub.
         Stay well and take care!
       '''),
    'RE_OPEN_SCHED': CLOSED_['RE_OPEN_SCHED']
 },
'location-waukee.html' : CLOSED_,
'':
    {
    'RE_OPEN': reopen_block('''
    The Westview church has informed us that outside
    activities will be suspended through June, and maybe
    longer.  Please consider the Clive/WDM branch location,
    or any other branch that is open for in-person classes.
    Mr. Dale and Mr. Ochiche will be teaching classes
    at the Clive/WDM location until the Waukee location is
    able to reopen. Be sure to check the other branch pages
    for details before coming to a class and consider
    participating in online classes as well. 
    ''')
    },
'location-wdm.html' : 
    {
    'RE_OPEN': reopen_block('''
    We are holding
    2 classes, 45 minutes each, at 5:45pm and 6:45pm
    Monday through Thursday, and one class on
    Saturday mornings at 10am.  These classes will have limited size and initially
    require masks be worn.  To attend, you must sign up in advance
    to reserve your spot.  Here is the link for 
    <a href="https://www.signupgenius.com/go/5080c44a5ab23aaf49-february">February</a>
    and for
    <a href="https://www.signupgenius.com/go/5080c44a5ab23aaf49-march">March</a>.
    Please arrive wearing your dobok if
    possible and bring your own water bottle.
    <br/>
    <br/>
    For new students, please contact us by email
    at wdm@tworiversmartialarts.com or 
    <a href="contact.html">phone</a> to arrange for
    introductory classes, either in person or online.
    ''')
    },
'location-winterset.html' : {
    'RE_OPEN': reopen_block('''
        We have been monitoring the 14-day and 7-day positivity rates in Madison county.
        As of February 12th, the 14-day positivity rate had dropped below 10%. This means:
        <div style="font-weight:bold; padding-left: 25px">
        <ul>
        <li>We will re-open for in-person classes on Monday, February 15th </li>
        <li>Regular, in-person classes will follow every Monday and Wednesday evening-
           from 7 - 8 pm</li>
        <li>We will follow Covid protocols for masks and social distancing.
            Enhanced cleaning procedures will be followed each class. </li>
        </ul>
        </div>
        We will remain open for in-person classes as long as the 7-day positivity
        rate for Madison county remains at or below 10%. If that rate goes above 10%,
        we will close again. If you have any questions, contact the branch instructor.
      '''),
    'RE_OPEN_SCHED': reopen_block('') 
}
}
