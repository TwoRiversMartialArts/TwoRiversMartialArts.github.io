
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
     ''' and
     '''
     Carlisle branch is suspending in-person classes beginning on August 9th, 2021
     due to covid-19 test positivity rate above 10% in Warren county.  Classes will
     resume when this falls below 10%.
     '''),
    'RE_OPEN_SCHED': reopen_block('') 
 },
'location-hub.html' : {
    'RE_OPEN_SCHED': reopen_block(''),
    'RE_OPEN': reopen_block('''
    <p>
    The Hub location is holding in-person classes. Please follow
    <a href="https://www.signupgenius.com/go/904054ba4a629a0ff2-hub7">
    this link for August</a> and
    <a href="https://www.signupgenius.com/go/904054ba4a629a0ff2-hub8">
    this link for September</a>.
    </p><br/>
    <p>
    In person classes will look different. 
    </p>
    <div style="margin-top:6px; margin-left:23px; margin-bottom:10px">
    <ul>
      <li>Class sizes will be restricted to a limited number of
      students for the time being
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
      ''' and '''
      Indianola Branch is suspending in-person classes on Monday, August 9th, 2021.
      The 7-day positivity rates in Warren County as of August 9th, 2021, was elevated up to
      10%.
      This means-
      <ul><li>
       All classes will be closed until the positivity rate drops below 10%.
      </li><li>
       We will remain closed for in-person classes if the 7-day positivity rate for Warren County
      remains at or above 10%.
      </li><li>
       As soon as that rate goes below 10%, we will re-open again. That could be as soon as
      the next regularly scheduled class.
      </li><li>
       Monitor Indianola Branch Two Rivers Martial Arts on Facebook for updates.
      Additionally, updates will be posted on the door to the dojang.
      </li></ul>
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
'location-waukee.html' :
    {
    'RE_OPEN': reopen_block('''
       The Waukee branch will reopen for in person classes starting Tuesday, July 20th, 2021.
       Masks will be required for students attending this class.  Waukee will not have a
       sign up sheet to register for classes, our space is large enough to accommodate
       students with distance between them.  Classes will be at 6:30 P.M. to 7:30 P.M.
       Tuesdays and Thursdays.
    ''')
    },
'location-wdm.html' : 
    {
    'RE_OPEN': reopen_block('''
    We are holding
    2 classes, one hour each, at 5:45pm and 6:45pm
    Monday through Thursday, and one class on
    Saturday mornings at 10am.  These classes will have limited size.
    The 5:45pm classes and Saturday classes will require masks.
    The 6:45pm classes will not require masks for those who are
    vaccinated. To attend, you must sign up in advance
    to reserve your spot.  Here is the 
    <a href="https://www.signupgenius.com/go/5080c44a5ab23aaf49-september1">link for September</a>.
    and the
    <a href="https://www.signupgenius.com/go/5080c44a5ab23aaf49-october1">link for October</a>.
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
      ''' and 
      '''
      Winterset Branch is suspending in-person classes on Monday, August 9th, 2021.
      The 7 -day positivity rates in Madison County as of August 9th, 2021, was elevated up to
      14%.
      This means-
      <ul>
      <li>All classes will be closed until the positivity rate drops below 10%.
      </li><li>
      We will remain closed for in-person classes if the 7-day positivity rate for Madison
      County remains at or above 10%.
      </li><li>
      As soon as that rate goes below 10%, we will re-open again. That could be as soon as
      the next regularly scheduled class.
      </li><li>
      Monitor Two Rivers Martial Arts Winterset Branch on Facebook for updates.
      </li></ul> 
      '''
      ),
    'RE_OPEN_SCHED': reopen_block('') 
}
}
