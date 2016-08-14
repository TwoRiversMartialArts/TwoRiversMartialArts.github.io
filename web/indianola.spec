
<%%BranchName%%>~Indianola
@@@
<%%LATLNG%%>~41.361352, -93.578426
@@@
li(.*?indianola.*?Indian)~li class="navOn"\1
@@@
<%%picture%%>~
<div class="topofpage">
<!-- <img src="/web/gallery/wdm.jpg"></img> -->
</div>
@@@
<%%Monday%%>~
<ul>
    <li>Little Dragons<ul><li>6:00pm - 6:30pm</li></ul></li>
    <li>Beginner TKD<ul><li>6:00pm - 7:00pm</li></ul></li>
    <li>Advanced TKD<ul><li>7:00pm - 8:00pm</li></ul></li></ul>
@@@
<%%Wednesday%%>~
<ul>
  <li> Advanced TKD<ul><li>6:00pm - 7:00pm</li></ul></li>
  <li> Adult/Family<ul><li>7:00pm - 8:00pm</li></ul></li>
</ul>
@@@
<%%Thursday%%>~
<ul>
    <li>Little Dragons<ul><li>6:00pm - 6:30pm</li></ul></li>
    <li>Beginner TKD<ul><li>6:00pm - 7:00pm</li></ul></li>
    <li>Advanced TKD<ul><li>7:00pm - 8:00pm</li></ul></li></ul>
@@@
<%%.*?day%%>~&nbsp;
@@@

<%%Sched_Detail%%>~
<br/>
<a href="http://announce.trma.us/home/LittleDragons">
<img style="height:100px;padding-right:35px;padding-left:15px;float:left"
src="https://sites.google.com/a/trma.us/imagehosting/branches/indianola/littledragons.png"></img>
</a>
<br/>
A new class for 4 through 6 year olds is offered each two month session starting 
on October 12th, 2015.
The class meets Mondays and Thursdays 6:00 - 6:30pm.  
This is a specialized class tailored for children.  
Students will learn respect, gain strength, coordination, concentration, 
self-confidence, and increase attention span.  Use the
<a href="#&contactus">contact information</a>
below to request more
information.  See the announcement <a href="http://announce.trma.us/home/LittleDragons">
here</a>.
<br/><br/>
@@@

(?ms)<table.class..cost.*?<.table>~
The Indianola Parks and Rec department runs class registration and
collects payments.  See the Indianola
<a href="https://apm.activecommunities.com/cityofindianola/Activity_Search">
activity search page</a>, or the <a href="http://www.indianolaiowa.gov/309/Programs-Events">
events page</a>.
@@@
<%%instructors%%>~
<br/>
<ul>
<li><a href="instructors-primary.html#&SamuelsonM">Master Marvin Samuelson</a></li>
<li><a href="instructors-primary.html#&NetschR">Master Roger Netsch</a></li>
<li><a href="instructors-primary.html#&AndersonB">Mr. Brian Anderson</a></li>
<li><a href="instructors-primary.html#&LerchCh">Mr. Chris Lerch</a></li>
<li><a href="instructors-primary.html#&LerchCi">Ms. Cindy Lerch</a></li>
<li><a href="instructors-primary.html#&StJohnZ">Mr. Zachary St. John</a></li>
</ul>

@@@
<%%address%%>~
<div class="address">
<!-- Indianola Parks & Recreation<br/>
2204 West 2nd Street<br/>
Indianola, Iowa 50125<br/> 
Indianola East Dojang<br/>
1204 East 2nd Ave., Hwy 92,<br/> -->
Whittier Elementary Gym</br>
1306 W Salem Ave<br/>
Indianola, IA 50125<br> 
</div>
@@@
<%%moreinfo%%>~
<br/><br/>
<a name="contactus"></a><div class="moreinfo">
Contact Doug Byland through the Department of Parks & Recreation for further information.
<br/>
or email 
indianola@tworiversmartialarts.com <br/>
</div>
@@@
(?s)PAYMENT_INFO.*?PAYMENT_INFO~PAY_INFO
@@@
# remove all left over tags
<%%.*?%%>~ <!-- -->

