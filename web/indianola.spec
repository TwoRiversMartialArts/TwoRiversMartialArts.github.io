
<%%BranchName%%>~Indianola
@@@
<%%LATLNG%%>~41.356169,-93.588889
@@@
li(.*?indianola.*?Indian)~li class="navOn"\1
@@@
<%%picture%%>~
<div class="topofpage">
<!-- <img src="/web/gallery/wdm.jpg"></img> -->
</div>
@@@
<%%Monday%%>~
<ul><li>Beginner<ul><li>6:00pm - 7:00pm</li></ul></li>
             <li>Advanced<ul><li>7:00pm - 8:00pm</li></ul></li></ul>
@@@
<%%Wednesday%%>~
Advanced<br/>6:00pm - 7:00pm
@@@
<%%Thursday%%>~
<ul><li>Beginner<ul><li>6:00pm - 7:00pm</li></ul></li>
             <li>Advanced<ul><li>7:00pm - 8:00pm</li></ul></li></ul>
@@@
<%%.*?day%%>~&nbsp;
@@@
(?ms)<table.class..cost.*?<.table>~
The Indianola Parks and Rec department runs class registration and
collects payments.  See the city 
<a href="http://www.indianolaiowa.gov/Calendar.aspx">
calendar</a> for announcements of registration deadlines
and fees.  You can <a href="http://www.indianolaiowa.gov/SearchResults.aspx?Search=Two+Rivers">search the city's site for "Two Rivers"</a>
and find past and current announcements.

@@@
<%%instructors%%>~
<br/>
<ul>
<li><a href="instructors-primary.html#&SamuelsonM">Master Marvin Samuelson</a></li>
<li><a href="instructors-primary.html#&NetschR">Mr. Roger Netsch</a></li>
<li><a href="instructors-primary.html#&AndersonB">Mr. Brian Anderson</a></li>
</ul>

@@@
<%%address%%>~
<div class="address">
Indianola Parks & Recreation<br/>
2204 West 2nd Street<br/>
Indianola, Iowa 50125<br/>
</div>
@@@
<%%moreinfo%%>~
<br/><br/>
<div class="moreinfo">
Contact Doug Byland through the Department of Parks & Recreation for further information.
<br/>
or email 
indianola@tworiversmartialarts.com <br/>
</div>
@@@
# remove all left over tags
<%%.*?%%>~ <!-- -->

