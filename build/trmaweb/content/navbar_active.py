
A='active'
context = {}

def main() :
    global A, context, addins
    for br in 'carlisle wdm hub indianola winterset pleasanthill trma'.split() :
       context.setdefault('location-'+br+'.html',{})['LOCATIONS_active']=A
    for tmp, add in addins.items() :
       context.setdefault(tmp,{}).update(add)

addins = {
 'awards.html': 
    {'AWARDS_active':A,'ABOUT_active':A},
 'startingtkd.html' : 
    { 'ABOUT_active' : A, 'STARTING_active': A },
 'blackbeltlist.html' :  
    {'ABOUT_active' : A,'LISTOFBB_active' : A},
 'calendar.html' :  
    {'CALENDAR_active' : A },
 'community.html' :  
    {'ABOUT_active' : A,'OUTREACH_active' : A},
 'competition.html' : 
    {'ABOUT_active' : A,'COMPETITION_active' : A},
 'contact.html' :  
    { 'CONTACT_active' : A },
 'curriculum.html' : 
    { 'CURRICULUM_active' : A, 'ABOUT_active':A },
'history-trma.html' : 
    {'ABOUT_active' : A,'ABOUTTRMA_active' : A},
'index.html' : 
    { 'HOME_active' : A },
'instructors-primary.html' : 
    {'ABOUT_active' : A,'INSTRUCTORS_active' : A},
'kobudo.html' : 
    { 'KOBUDO_active' : A },
'location-carlisle.html' : 
    {'CARLISLE_active':A},
'location-hub.html' : 
    {'HUB_active':A},
'location-indianola.html' : 
    {'INDIANOLA_active':A},
'location-pleasanthill.html' : 
    {'PH_active':A},
'location-trma.html' : 
    {'TRMALOC_active':A},
'location-wdm.html' : 
    {'WDM_active':A},
'location-winterset.html' : 
    {'WINTERSET_active':A},
'martial-spirit.html' : 
    { 'MS_active' : A },
'portfolio.html' : 
    {},
'resource-tenets.html' : 
    { 'RESOURCES_active' : A, 'TENETS_active' : A },
'resource-terminology.html' : 
    { 'RESOURCES_active' : A , 'TERM_active' : A },
'taichi.html' : 
    {'TC_active' : A },
'tkdt-bbyg.html' : 
    { 'BBYG_active' : A },
'ybbc.html' : 
    { 'BBYG_active' : A }
}
main()

