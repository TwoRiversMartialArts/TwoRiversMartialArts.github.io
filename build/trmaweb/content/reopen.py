
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
January 18th. 
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
        In-person classes are suspened.
        ''')
    }

context = {
 'locations-trma.html' :
    {
        #'RE_OPEN' : reopen_block('''
        #Each branch page will include
        #details of available in-person classes at the top of the page.
        #'''),
        #'RE_OPEN_SCHED' : reopen_block('''
        #Please visit the individual branch pages for
        #accurate information regarding class schedules
        #amid the COVID-19
        #pandemic.  Each page will have a notice like
        #this one at the top of the page.
        #''')
    },
 'location-carlisle.html' : {
    #'RE_OPEN': reopen_block('''
    #Good news. The Carlisle branch is open for classes again.
    #<br/><br/>
    #Hope to see you there.
     #'''),
    #'RE_OPEN_SCHED': reopen_block('') 
 },
'location-hub.html' : {
    #'RE_OPEN_SCHED': reopen_block(''),
    #'RE_OPEN': reopen_block('''
    #<p>
    #The Hub location is holding in-person classes. Please follow
    #<a href="https://www.signupgenius.com/go/10c0f44a9aa29a7f4c16-august">
    #this link for August</a> class signups.
    #</p><br/>
    #<p>
    #The class schedule and teaching schedule may be adjusted if
    #needed depending upon interest.
    #</p><br/>
    #</div>
    #''')
    },
'location-indianola.html' : {
    #'RE_OPEN': reopen_block('''
       #Classes have resumed for all belt levels.
       #Face masks are optional. If you are not feeling well, please stay home.
       #Otherwise we'll see you at our new location at Fusion Fitness on the south
       #side of the Square in Indianola. Class times will be the same as they've
       #always been. Beginner and Advanced classes are on Mondays and Thursday
       #evenings. Beginners start at 6 pm and colored belts at 7 pm.
       #There is a colored belt class on Wednesdays from 6:30-7:30 pm.
       #There is a changing room available.
       #<br><br>
       #Due to construction on the Square, access to the front (North) side of
       #the building may be limited. Not to worry, there is a back door on the
       #back (South) side of the building in the alley. Parking is available
       #on the street or in a public lot adjacent to the alley where the back
       #entrance to Fusion is located. This parking lot is north or across
       #the street from the Legion Building near the post office.
      #'''),
    #'RE_OPEN_SCHED': reopen_block('') 
    },
'location-pleasanthill.html' : {
    #'RE_OPEN': reopen_block('''
       #Due to the pandemic, the Pleasant Hill branch will not be holding
       #classes until further notice. Please consider our other branch
       #locations.
       #'''),
    #'RE_OPEN_SCHED': CLOSED_['RE_OPEN_SCHED']
 },
'location-waukee.html' :
    {
    #'RE_OPEN': reopen_block('''
       #The Waukee branch is open for classes.
       #Classes will be at 6:30 P.M. to 7:30 P.M.
       #Tuesdays and Thursdays.
    #''')
    },
'location-wdm.html' : 
    {
    #'RE_OPEN': reopen_block('''
    #We are holding
    #2 classes, one hour each, at 5:45pm and 6:45pm
    #Monday through Thursday, and one class on
    #Saturday mornings at 10am. 
    #Wearing a mask in class is optional.  If a minor child enters
    #wearing a mask, the instructor will assume the parent desires
    #the child to wear the mask throughout the class and will require
    #them to do so.

    #Please arrive wearing your dobok if
    #possible and bring your own water bottle.
    #''')
    },
'location-winterset.html' : {
    #'RE_OPEN': reopen_block(
      #'''
      #Colored belt classes are scheduled for
      #Monday and Wednesday evenings from 7 to 8 pm. Beginners and others,
      #try to arrive 10-15 minutes earlier.
      #'''
      #),
    #'RE_OPEN_SCHED': reopen_block('') 
    },
'taichi.html' : {
    #'RE_OPEN': reopen_block('''
       #Due to the pandemic Tai Chi classes are temporarily suspended.''')
    },
'kobudo.html' : {
    #'RE_OPEN': reopen_block('''
       #Due to the pandemic Kobudo classes are temporarily suspended.''')
}
}
