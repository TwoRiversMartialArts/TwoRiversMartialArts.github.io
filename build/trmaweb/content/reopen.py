
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

context = {
 'locations-trma.html' :
    {
        'RE_OPEN' : reopen_block('''
        Each branch page will include re-opening
        details at the top of the page.
        '''),
        'RE_OPEN_SCHED' : reopen_block('''
        Please visit the individual branch pages for
        accurate information regarding class schedules
        during our re-opening phase amid the COVID-19
        pandemic.  Each page will have a notice like
        this one at the top of the page.
        ''')
    },
 'location-carlisle.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    Classes will resume by July 1st.
    </p><br/>
    <p> 
    Below are the guidelines that will be followed when
    classes start back up.
    </p><br/>
    <div style="margin-left:23px">
    <ul>
    <li>
    Class sizes will be restricted to 25 students for the time
    being in order to maintain social distancing.  </li>
    <li>If at all possible, students should arrive in their Dobok.
    </li>
    <li>Students should bring their own bottle of water.
    The water fountain will be off limits for now.
    </li>
    <li>Face masks, bandannas, or other alternative face
    coverings will be required. Triple layer Ninja masks anyone? :)
    </li>
    <li>Shoes may be required. This is still being evaluated.
    </li>
    <li>Because face masks will be required, classes will be more
       technique based and less cardio based.
    </li>
    <li>Students are strongly encouraged to attend online classes for
    the cardio component.
    </li>
    <li>Parents will be requested to wait outside of the building.</li>
    <li>If the weather is good classes may be held outside.
    </li>
    <li>There will be no sparring or board breaking and
        one steps and self defense will be without a
        partner unless they are members of a family.
    </li>
    <li>
    If the weather is good classes will be held outside.
    If you want to wear a T-shirt those days to stay cooler
    then come dressed with the T-Shirt under your Dobok.
    The T-shirt can be either a Carlisle/Pleasant Hill/TRMA logo shirt.
    Otherwise it should be a single colored shirt with
    no pictures or writings.
    </li>
    </ul></div>
    </p><br/><p> 
    Cleaning will be performed between classes.
    If you have any questions, concerns or suggestions please let
    the instructors know. We want to make this as safe as possible
    and have everyone feeling at ease.
    </p>
    ''')
    },
'location-hub.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    The Hub location will begin holding classes on June 17th. Please follow
    <a href="https://www.signupgenius.com/index.cfm?go=c.SignUpSearch&eid=00CBCFD7F5CFFD67&cs=09C3BAAD8FBB8B627B0A64715BB29BC9&sortby=&view=i">
    this link for signups</a>, or view the
    <a href="https://drive.google.com/file/d/1XPM6DtTLKPrEREDXsLW2WrvM5XqTI3qp/view">
    instructions</a> to search for the signup pages.
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
'location-indianola.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    We will be reopening the Indianola dojang on June 8th,
    running 2 classes as usual ... white belts from 6-7 pm
    and colored belts from 7-8 pm.
    </p>

    <ul style="margin: 15px"> 
     <li>Monday 6-7 pm White and 7-8 pm all others</li>
     <li>Thursday 6-7 pm white and 7-8 pm all others</li>
    </ul>

    <p>
    Below are the guidelines that will be followed as
    classes start back up at Indianola.
    </p>
    <ul style="margin: 15px"> 
    <li>  Class sizes may be restricted for the time being in order to maintain social distancing.
    </li>  
    <li>If possible, students should arrive in their dobok (uniform).
    </li>
    <li>Students should bring their own bottle of water. The water fountain will be off limits for now.
    </li>
    <li>Face masks, bandannas, or other alternative face coverings will be required.
    </li>
    <li>Because face masks will be worn, classes will be more technique based and less
    cardio based.  Students are strongly encouraged to attend online classes for
    the cardio component.
    </li>
    <li>Parents will be requested to wait outside of the building.
    </li>
    <li>There will be no sparring or board breaking and one-steps and self-defense will
    be without a partner unless there are members of a family present.
    </li>
    </ul>

    <div style="font-weight:bold; font-size:150%; text-align: center">
    <p>
    We all hope these adjustments to class will be only
    temporary for the safety of all. We will resume regular
    classes as soon as possible.
    </p>
    </div>

    <p>Curriculum:</p>
    <ul style="margin: 15px"> 
    </li>
    <li>Kicking
    </li>
    <li>Punching
    </li>
    <li>Basic/advanced movements modified for social distance
    </li>
    <li>Forms
    </li>
    <li>Shadow one steps
    </li>
    <li>Shadow Self-defense
    </li>
    <li>Shadow sparring
    </li>
    <li>Other</li>
    </ul>
    ''')

    },
'location-pleasanthill.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    Classes are  resuming Wednesday, July 1st.
    The Pleasant Hill branch will be joining the Carlisle
    branch during this time. Our location is:
    </p><br/>
     Parks and Rec building<br/>
     1220 S. 5th St.<br/>
     Carlisle, IA 50047<br/>
     Monday and Wednesday <br/>
     6:30-7:30<br/><br/>

     <p>
     Class guidelines and curriculum is listed on the
     <a href="location-carlisle.html">
     Carlisle branch page</a>. Please review these before
     attending class.
     </p>
    ''')
    },
'location-waukee.html' : 
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
    The new location is ready for operations! We are planning
    to hold 2 classes, 45 minutes each, at 5:45pm and 6:45pm
    Monday through Thursday, and at least one class on
    Saturday mornings at 10am.  These classes will have limited size and initially
    require masks be worn.  To attend, you must sign up in advance
    to reserve your spot.  Here is the link for 
    <a href="https://www.signupgenius.com/go/5080c44a5ab23aaf49-october">October</a>.
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
'location-winterset.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    Below are the guidelines that will be followed
    as classes start back up at Winterset on July 1, 2020:
    </p>
    <ul style="margin: 15px"> 
    <li>  Class sizes may be restricted for the time being in order to maintain social distancing.
    </li>  
    <li>If possible, students should arrive in their dobok (uniform).
    </li>
    <li>Students should bring their own bottle of water. The water fountain will be off limits for now.
    </li>
    <li>Face masks, bandannas, or other alternative face coverings will be required.
    </li>
    <li>Because face masks will be worn, classes will be more technique based and less
    cardio based.  Students are strongly encouraged to attend online classes for
    the cardio component.
    </li>
    <li>Parents will be requested to social distance while waiting for
        their children. 
    </li>
    <li>If weather is good, classes may be held outside.</li>
    <li>There will be no sparring or board breaking and one-steps and self-defense will
    be without a partner unless there are members of a family present.
    </li>
    </ul>

    <div style="font-weight:bold; font-size:150%; text-align: center">
    <p>
    We all hope these adjustments to class will be only
    temporary for the safety of all. We will resume regular
    classes as soon as possible.
    </p>
    </div>

    <p>Curriculum:</p>
    <ul style="margin: 15px"> 
    </li>
    <li>Kicking
    </li>
    <li>Punching
    </li>
    <li>Basic/advanced movements modified for social distance
    </li>
    <li>Forms
    </li>
    <li>Shadow one steps
    </li>
    <li>Shadow Self-defense
    </li>
    <li>Shadow sparring
    </li>
    <li>Other</li>
    </ul>
    ''')
    }
}
