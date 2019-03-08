
context = {

 'location-wdm.html' : {
    'class_schedule' : [
       { 'day' : 'Tuesday',
         'classes' : [( 'TKD','6:15 PM - 7:15 PM')]},
       { 'day' : 'Thursday',
         'classes' : [( 'TKD', '6:15 PM - 7:15 PM')]}
      ]
   },

 'location-carlisle.html' : {
    'class_schedule' : [
       { 'day' : 'Monday',
         'classes' : [( 'TKD','6:30 PM - 7:30 PM')]},
       { 'day' : 'Wednesday',
         'classes' : [( 'TKD', '6:30 PM - 7:30 PM')]}
      ]
   },

 'location-winterset.html' : {
    'class_schedule' : [
       { 'day' : 'Monday',
         'classes' : [( 'TKD','7:00 PM - 8:00 PM')]},
       { 'day' : 'Wednesday',
         'classes' : [( 'TKD', '7:00 PM - 8:00 PM')]}
      ]
   },

 'location-pleasanthill.html' : {
    'class_schedule' : [
       { 'day' : 'Tuesday',
         'classes' : [( 'TKD','6:30 PM - 7:30 PM')]},
       { 'day' : 'Thursday',
         'classes' : [( 'TKD', '6:15 PM - 7:15 PM')]}
      ]
   },

 'location-indianola.html' : {
    'class_schedule' : [
       { 'day' : 'Monday',
         'classes' : [( 'Little Dragons','5:30 PM - 6:00 PM'),
                      ( 'Beginner TKD','6:00 PM - 7:00 PM'),
                      ( 'Advanced TKD','7:00 PM - 8:00 PM')]},
       { 'day' : 'Wednesday',
         'classes' : [( 'Colored Belts', '6:00 PM - 7:00 PM'),
                      ( 'Adults', '7:00 PM - 8:00 PM')]},
       { 'day' : 'Thursday',
         'classes' : [( 'Little Dragons','5:30 PM - 6:00 PM'),
                      ( 'Beginner TKD','6:00 PM - 7:00 PM'),
                      ( 'Advanced TKD','7:00 PM - 8:00 PM')]}
      ]
   },

   'location-hub.html' : {
     'class_schedule' : [
     ]
   }
}
hub = context['location-hub.html']['class_schedule']

for day in ('Monday','Tuesday','Wednesday','Thursday') :
  hub.append(
     { 'day' : day,
       'classes' : [('TKD','6:00 PM - 7:00 PM')] } )

hub.append( { 'day' : 'Friday',
  'classes' : [('Brown/Black belt class',
                '6:00 PM - 7:30 PM')] } )
hub.append( { 'day' : 'Saturday',
  'classes' : [ ('Adult/Family TKD*','10:00 AM - 11:00 AM'),
                ('TKD','11:15 AM - 12:15 PM'),
                ('Black Belt Youth Group',
                 '1:00 PM or 3:00 PM on 2<sup>nd</sup> '
                 'Saturday of each month***') 
              ] } )
hub.append( { 'day' : 'Sunday' ,
  'classes' : [
      ('Martial Spirit','9:30 AM - 12:00 noon'),
      ('Tai Chi','12:00 noon - 1:00 PM'),
      ('Kobudo','1:00 PM - 3:00 PM'),
      ('Brown/Black belt class','3:00 PM - 4:30 PM')
    ] })

