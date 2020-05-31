
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
    Please check back soon for re-opening plans!
    ''')
    },
'location-hub.html' : 
    {
    'RE_OPEN': reopen_block('''
    Please check back soon for re-opening plans!
    ''')
    },
'location-indianola.html' : 
    {
    'RE_OPEN': reopen_block('''
    <p>
    We will be reopening the Indianola dojang on June 4th,
    running 2 classes as usual ... white belts from 6-7 pm
    and colored belts from 7-8 pm.
    </p>

    <ul style="margin: 15px"> 
     <li>Monday 6-7 pm White and 7-8 pm all others</li>
     <li>Wednesday 6-7 pm all belt levels</li>
     <li>Thursday 6-7 pm white and 7-8 pm all others</li>
    </ul>

    <p>
     We may do lower belts in the earlier class and higher
     belts in the later, but we'll see how many people turn out first.
     There will be no Little Dragons classes for the time being.
     There will be no additional workout after class to allow
     time for adequate cleaning.
    </p>
    <p>
    People will be spread out on the floor and we will be practicing
    enhanced cleaning of the dojang. It is our students' choice
    to participate at the dojang. If they feel that it's unsafe
    they may participate in the Zoom classes.
    </p>
    ''')

    },
'location-pleasanthill.html' : 
    {
    'RE_OPEN': reopen_block('''
    Please check back soon for re-opening plans!
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
    Saturday mornings.  These classes will have limited size and initially
    require masks be worn.  To attend, you must sign up in advance
    to reserve your spot.  Wednesday, June 3rd, will be the
    first class date. We will have links here to the sign-up
    page very soon. 
    ''')
    },
'location-winterset.html' : 
    {
    'RE_OPEN': reopen_block('''
    Please check back soon for re-opening plans!
    ''')
    }
}
