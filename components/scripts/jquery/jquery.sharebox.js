/*!
 * jQuery Sharebox plugin
 * http://www.dontblink.net/
 * Author: K.S. Gerstenberger
 *
 * Date: Tue Feb 16 10:09:05 2010 -0600
 */


(function($) {
    $.fn.sharebox = function(vpos, hpos, sprite) {
        var element = this;
        $(element).click(function() { return false; });
        var sbox = ".sharebox";
        var sitem = "p.shareitem";
        var position = $(element).position();
        var newVpos, newHpos
        if (sprite == "" || sprite == null) { sprite = "sharebox-sprites.gif"; }

        var newStyle = "div" + sbox + " { width: 252px; height:90px; display:none; z-index:100; background-color:#efefef; border:solid 1px #666; position: absolute; top:0px; left:0px;display:none;}div" + sbox + " ul { width: 250px; margin: 0; padding: 0; list-style: none; display:block; }div" + sbox + " li { float: left; margin:0px; padding:0px; line-height:16px;}div" + sbox + " p.shareitem { background:url('" + sprite + "') no-repeat;margin:12px 12px 0 13px; padding:0px; height: 16px; width:16px; cursor:hand;}div" + sbox + " div.pageButtons {position: absolute;left:0;bottom:0;width:100%;background-color:#999;height:20px;border-top:solid 1px #666;}div" + sbox + " div.pageLeft, div" + sbox + " div.pageRight {float:right;cursor:hand;color:#fff;height:20px;padding-left:5px;padding-right:5px;font-weight:bold;}";
        newStyle = newStyle + "div" + sbox + " p.ballhype { background-position: 0px -80px; }div" + sbox + " p.bebo { background-position: 0px -880px; }div" + sbox + " p.diigo { background-position: 0px -896px; }div" + sbox + " p.multiply { background-position: 0px -864px; }div" + sbox + " p.propeller { background-position: 0px -32px; }div" + sbox + " p.tailrank { background-position: 0px -32px; }div" + sbox + " p.myaol { background-position: 0px -16px; }div" + sbox + " p.mailto { background-position: 0px -224px; }div" + sbox + " p.feedmelinks { background-position: 0px -831px; }div" + sbox + " p.live { background-position: 0px -416px; }div" + sbox + " p.buzz { background-position: 0px -160px; }div" + sbox + " p.myweb2 { background-position: 0px -512px; }div" + sbox + " p.ask { background-position: 0px -48px; }div" + sbox + " p.spurl { background-position: 0px -688px; }div" + sbox + " p.yardbarker { background-position: 0px -816px; }div" + sbox + " p.kaboodle { background-position: 0px -352px; }div" + sbox + " p.segnalo { background-position: 0px -608px; }div" + sbox + " p.simpy { background-position: 0px -640px; }div" + sbox + " p.backflip { background-position: 0px -64px; }div" + sbox + " p.blinklist { background-position: 0px -112px; }div" + sbox + " p.blogmarks { background-position: 0px -128px; }div" + sbox + " p.delicious { background-position: 0px -176px; }div" + sbox + " p.digg { background-position: 0px -192px; }div" + sbox + " p.facebook { background-position: 0px -240px; }div" + sbox + " p.fark { background-position: 0px -256px; }div" + sbox + " p.faves{ background-position: 0px -144px; }div" + sbox + " p.friendfeed { background-position: 0px -304px; }div" + sbox + " p.furl { background-position: 0px -320px; }div" + sbox + " p.google { background-position: 0px -336px; }div" + sbox + " p.linkagogo { background-position: 0px -384px; }div" + sbox + " p.linkedin { background-position: 0px -400px; }div" + sbox + " p.magnolia{ background-position: 0px -432px; }div" + sbox + " p.mixx { background-position: 0px -464px; }div" + sbox + " p.myspace { background-position: 0px -496px; }div" + sbox + " p.netvouz { background-position: 0px -528px; }div" + sbox + " p.newsvine { background-position: 0px -544px; }div" + sbox + " p.pownce { background-position: 0px -560px; }div" + sbox + " p.propeller { background-position: 0px -576px; }div" + sbox + " p.reddit { background-position: 0px -592px; }div" + sbox + " p.slashdot { background-position: 0px -672px; }div" + sbox + " p.stumbleupon { background-position: 0px -704px; }div" + sbox + " p.technorati { background-position: 0px -752px; }div" + sbox + " p.twitter { background-position: 0px -784px; }div" + sbox + " p.yahoo { background-position: 0px -512px; }";
        newStyle = newStyle + "div" + sbox + " p.yigg { background-position: 0px -912px; }div" + sbox + " p.fresqui { background-position: 0px -976px; }div" + sbox + " p.dealsplus { background-position: 0px -1168px; }div" + sbox + " p.n4g { background-position: 0px -944px; }div" + sbox + " p.funp { background-position: 0px -960px; }div" + sbox + " p.care2 { background-position: 0px -1024px; }div" + sbox + " p.kirtsy { background-position: 0px -1008px; }div" + sbox + " p.wong { background-position: 0px -992px; }div" + sbox + " p.meneame { background-position: 0px -1088px; }div" + sbox + " p.oknotizie { background-position: 0px -1072px; }div" + sbox + " p.aim { background-position: 0px -1056px; }div" + sbox + " p.current { background-position: 0px -1040px; }div" + sbox + " p.twackle { background-position: 0px -1104px; }div" + sbox + " p.xanga { background-position: 0px -1120px; }div" + sbox + " p.twine { background-position: 0px -1136px; }div" + sbox + " p.ybookmarks { background-position: 0px -1152px; }div" + sbox + " p.sphinn { background-position: 0px -928px; }";

        $("<style>" + newStyle + "</style>").appendTo("body");

        var newBox = "<div class='sharebox'>";
        newBox = newBox + "<ul class='page1'><li><p class='shareitem mailto' title='Send Email'>&nbsp;</p></li><li><p class='shareitem facebook' title='Facebook'>&nbsp;</p></li><li><p class='shareitem twitter' title='Twitter'>&nbsp;</p></li><li><p class='shareitem stumbleupon' title='StumbleUpon'>&nbsp;</p></li><li><p class='shareitem reddit' title='reddit'>&nbsp;</p></li><li><p class='shareitem google' title='Google'>&nbsp;</p></li><li><p class='shareitem linkedin' title='LinkedIn'>&nbsp;</p></li><li><p class='shareitem delicious' title='Delicious'>&nbsp;</p></li><li><p class='shareitem technorati' title='Technorati Favorites'>&nbsp;</p></li><li><p class='shareitem digg' title='Digg'>&nbsp;</p></li>          <li><p class='shareitem yigg' title='YiGG'>&nbsp;</p></li><li><p class='shareitem ybookmarks' title='ybookmarks'>&nbsp;</p></li>         </ul>";
        newBox = newBox + "<ul class='page2'><li><p class='shareitem spurl' title='Spurl'>&nbsp;</p></li><li><p class='shareitem ask' title='Ask - MyStuff'>&nbsp;</p></li><li><p class='shareitem magnolia' title='Gnolia'>&nbsp;</p></li><li><p class='shareitem diigo' title='Diigo'>&nbsp;</p></li><li><p class='shareitem blinklist' title='BlinkList.com'>&nbsp;</p></li><li><p class='shareitem kaboodle' title='kaboodle'>&nbsp;</p></li><li><p class='shareitem friendfeed' title='FriendFeed'>&nbsp;</p></li><li><p class='shareitem myspace' title='MySpace'>&nbsp;</p></li><li><p class='shareitem backflip' title='Backflip'>&nbsp;</p></li><li><p class='shareitem simpy' title='simpy'>&nbsp;</p></li>                          <li><p class='shareitem fresqui' title='fresqui'>&nbsp;</p></li><li><p class='shareitem care2' title='care2'>&nbsp;</p></li>         </ul>";
        newBox = newBox + "<ul class='page3'><li><p class='shareitem multiply' title='Multiply'>&nbsp;</p></li><li><p class='shareitem feedmelinks' title='Feed Me Links'>&nbsp;</p></li><li><p class='shareitem buzz' title='Yahoo! Buzz'>&nbsp;</p></li><li><p class='shareitem myweb2' title='myweb2'>&nbsp;</p></li><li><p class='shareitem yahoo' title='Yahoo'>&nbsp;</p></li><li><p class='shareitem yardbarker' title='Yardbarker'>&nbsp;</p></li><li><p class='shareitem netvouz' title='Netvouz'>&nbsp;</p></li><li><p class='shareitem newsvine' title='Newsvine'>&nbsp;</p></li><li><p class='shareitem slashdot' title='Slashdot'>&nbsp;</p></li><li><p class='shareitem blogmarks' title='Blogmarks'>&nbsp;</p></li>             <li><p class='shareitem dealsplus' title='dealspl.us'>&nbsp;</p></li><li><p class='shareitem kirtsy' title='kirtsy'>&nbsp;</p></li>         </ul>";
        newBox = newBox + "<ul class='page4'><li><p class='shareitem segnalo' title='Segnalo'>&nbsp;</p></li><li><p class='shareitem faves' title='Faves'>&nbsp;</p></li><li><p class='shareitem linkagogo' title='linkaGoGo'>&nbsp;</p></li><li><p class='shareitem mixx' title='Mixx'>&nbsp;</p></li><li><p class='shareitem myaol' title='myaol'>&nbsp;</p></li><li><p class='shareitem fark' title='FARK.com'>&nbsp;</p></li><li><p class='shareitem bebo' title='bebo'>&nbsp;</p></li><li><p class='shareitem propeller' title='Propeller'>&nbsp;</p></li><li><p class='shareitem ballhype' title='BallHype'>&nbsp;</p></li><li><p class='shareitem live' title='Windows Live'>&nbsp;</p></li>                                            <li><p class='shareitem sphinn' title='sphinn'>&nbsp;</p></li><li><p class='shareitem wong' title='Mr. Wong'>&nbsp;</p></li>         </ul>";
        newBox = newBox + "<ul class='page5'><li><p class='shareitem funp' title='funP'>&nbsp;</p></li><li><p class='shareitem twine' title='twine'>&nbsp;</p></li><li><p class='shareitem xanga' title='xanga'>&nbsp;</p></li><li><p class='shareitem twackle' title='twackle'>&nbsp;</p></li><li><p class='shareitem current' title='current'>&nbsp;</p></li><li><p class='shareitem aim' title='aim'>&nbsp;</p></li><li><p class='shareitem oknotizie' title='oknotizie'>&nbsp;</p></li><li><p class='shareitem meneame' title='meneame'>&nbsp;</p></li><li><p class='shareitem n4g' title='n4g'>&nbsp;</p></li></ul>";
        newBox = newBox + "<div class='pageButtons'><div class='pageRight' title='next page'> &raquo; </div><div class='pageLeft' title='previous page'> &laquo; </div></div>";
        newBox = newBox + "</div>";
        $(newBox).appendTo("body");

        try {
            if (vpos == "top") { newVpos = (position.top - $(sbox).height()); } else { newVpos = (position.top + $(element).height()); }
        } catch (err) { }

        try {
            if (hpos == "right") { newHpos = (position.left - $(sbox).width() + $(element).width()); } else if (hpos == "center") { newHpos = (position.left - ($(sbox).width() / 2) + ($(element).width() / 2)); } else { newHpos = (position.left); }
        } catch (err) { }

        $(element).click(function() { $(sbox).css({ "left": newHpos + "px", "top": newVpos + "px" }); if ($(sbox).is(':visible')) { $(sbox).animate({ opacity: "hide" }, "fast"); } else { $(sbox).animate({ opacity: "show" }, "slow"); $('ul.page1').animate({ opacity: "show" }, "fast"); $('ul.page2').hide(); $('ul.page3').hide(); $('ul.page4').hide(); $('ul.page5').hide(); } });
        $(sbox).mouseleave(function() { $(sbox).animate({ opacity: "hide" }, "fast"); });
        $("div.pageRight").click(function() { if ($('ul.page1').is(':visible')) { $('ul.page1').hide(); $('ul.page2').slideDown("slow"); } else if ($('ul.page2').is(':visible')) { $('ul.page2').hide(); $('ul.page3').slideDown("slow"); } else if ($('ul.page3').is(':visible')) { $('ul.page3').hide(); $('ul.page4').slideDown("slow"); } else if ($('ul.page4').is(':visible')) { $('ul.page4').hide(); $('ul.page5').slideDown("slow"); } else if ($('ul.page5').is(':visible')) { $('ul.page5').hide(); $('ul.page1').slideDown("slow"); } });
        $("div.pageLeft").click(function() { if ($('ul.page1').is(':visible')) { $('ul.page1').hide(); $('ul.page5').slideDown("slow"); } else if ($('ul.page2').is(':visible')) { $('ul.page2').hide(); $('ul.page1').slideDown("slow"); } else if ($('ul.page3').is(':visible')) { $('ul.page3').hide(); $('ul.page2').slideDown("slow"); } else if ($('ul.page4').is(':visible')) { $('ul.page4').hide(); $('ul.page3').slideDown("slow"); } else if ($('ul.page5').is(':visible')) { $('ul.page5').hide(); $('ul.page4').slideDown("slow"); } });

        $(sitem).click(function(ev) {
            var rel

            if ($(this).is('.stumbleupon')) {
                rel = "http://www.stumbleupon.com/submit?url={url}&title={title}";
            } else if ($(this).is('.facebook')) {
                rel = "http://www.facebook.com/sharer.php?u={url}&t={title}";
            } else if ($(this).is('.backflip')) {
                rel = "http://www.backflip.com/add_page_pop.ihtml?url={url}&title={title}";
            } else if ($(this).is('.blinklist')) {
                rel = "http://www.blinklist.com/index.php?Action=Blink/addblink.php&Url={url}&Title={title}";
            } else if ($(this).is('.blogmarks')) {
                rel = "http://blogmarks.net/my/new.php?mini=1&simple=1&url={url}&title={title}";
            } else if ($(this).is('.delicious')) {
                rel = "http://del.icio.us/post?v=4&partner=[partner]&noui&url={url}&title={title}";
            } else if ($(this).is('.digg')) {
                rel = "http://digg.com/submit?phase=2&partner=[partner]&url={url}&title={title}";
            } else if ($(this).is('.diigo')) {
                rel = "http://www.diigo.com/post?url={url}&title={title}";
            } else if ($(this).is('.fark')) {
                rel = "http://cgi.fark.com/cgi/fark/submit.pl?new_url={url}&new_comment={title}";
            } else if ($(this).is('.friendfeed')) {
                rel = "http://friendfeed.com/share?url={url}&title={title}";
            } else if ($(this).is('.furl')) {
                rel = "http://www.furl.net/savedialog.jsp?p=1&u={url}&t={title}&r=&v=1&c=";
            } else if ($(this).is('.google')) {
                rel = "http://www.google.com/bookmarks/mark?op=add&bkmk={url}&title={title}";
            } else if ($(this).is('.linkagogo')) {
                rel = "http://www.linkagogo.com/go/AddNoPopup?url={url}&title={title}";
            } else if ($(this).is('.linkedin')) {
                rel = "http://www.linkedin.com/shareArticle?mini=true&url={url}&title={title}&ro=false&summary=&source=";
            } else if ($(this).is('.magnolia')) {
                rel = "http://ma.gnolia.com/bookmarklet/add?url={url}&title={title}";
            } else if ($(this).is('.facebook')) {
                rel = "http://www.mister-wong.com/index.php?action=addurl&bm_url={url}&bm_description={title}";
            } else if ($(this).is('.mixx')) {
                rel = "http://www.mixx.com/submit?page_url={url}";
            } else if ($(this).is('.myspace')) {
                rel = "http://www.myspace.com/Modules/PostTo/Pages/?u={url}&t={title}&c=%20";
            } else if ($(this).is('.netvouz')) {
                rel = "http://netvouz.com/action/submitBookmark?url={url}&title={title}&popup=no";
            } else if ($(this).is('.newsvine')) {
                rel = "http://www.newsvine.com/_tools/seed&save?u={url}&h={title}";
            } else if ($(this).is('.reddit')) {
                rel = "http://reddit.com/submit?url={url}&title={title}";
            } else if ($(this).is('.slashdot')) {
                rel = "http://slashdot.org/bookmark.pl?url={url}";
            } else if ($(this).is('.technorati')) {
                rel = "http://technorati.com/faves/?add={url}";
            } else if ($(this).is('.twitter')) {
                rel = "http://twitter.com/home?status={url}";
            } else if ($(this).is('.yahoo')) {
                rel = "http://bookmarks.yahoo.com/toolbar/savebm?opener=tb&u={url}&t={title}";
            } else if ($(this).is('.faves')) {
                rel = "http://bluedot.us/Authoring.aspx?u={url}&t={title}";
            } else if ($(this).is('.ask')) {
                rel = "http://myjeeves.ask.com/mysearch/BookmarkIt?v=1.2&t=webpages&url={url}&title={title}";
            } else if ($(this).is('.spurl')) {
                rel = "http://www.spurl.net/spurl.php?url={url}&title={title}";
            } else if ($(this).is('.yardbarker')) {
                rel = "http://www.yardbarker.com/author/new/?pUrl={url}";
            } else if ($(this).is('.kaboodle')) {
                rel = "http://www.kaboodle.com/grab/addItemWithUrl?url={url}&pidOrRid=pid=&redirectToKPage=true";
            } else if ($(this).is('.segnalo')) {
                rel = "http://segnalo.com/post.html.php?url={url}&title={title}";
            } else if ($(this).is('.simpy')) {
                rel = "http://www.simpy.com/simpy/LinkAdd.do?href={url}&title={title}";
            } else if ($(this).is('.ballhype')) {
                rel = "http://ballhype.com/post/url/?url={url}&title={title}";
            } else if ($(this).is('.bebo')) {
                rel = "http://bebo.com/c/share?Url={url}&Title={title}";
            } else if ($(this).is('.feedmelinks')) {
                rel = "http://feedmelinks.com/categorize?from=toolbar&op=submit&url={url}&name={title}";
            } else if ($(this).is('.live')) {
                rel = "https://favorites.live.com/quickadd.aspx?marklet=1&mkt=en-us&url={url}&title={title}&top=1";
            } else if ($(this).is('.multiply')) {
                rel = "http://multiply.com/gus/journal/compose/?body=&url={url}&subject={title}";
            } else if ($(this).is('.myaol')) {
                rel = "http://favorites.my.aol.com/ffclient/AddBookmark?url={url}&title={title}&favelet=true";
            } else if ($(this).is('.propeller')) {
                rel = "http://www.propeller.com/submit/?U={url}&T={title}";
            } else if ($(this).is('.tailrank')) {
                rel = "http://tailrank.com/share/?link_href={url}&title={title}";
            } else if ($(this).is('.buzz')) {
                rel = "http://buzz.yahoo.com/submit?submitUrl={url}&submitHeadline={title}";
            } else if ($(this).is('.myweb2')) {
                rel = "http://myweb2.search.yahoo.com/myresults/bookmarklet?u={url}&t={title}";
            } else if ($(this).is('.yigg')) {
                rel = "http://www.yigg.de/neu?exturl={url}&exttitle={title}";
            } else if ($(this).is('.fresqui')) {
                rel = "http://fresqui.com/enviar?url={url}&title={title}";
            } else if ($(this).is('.dealsplus')) {
                rel = "http://dealspl.us/add.php?ibm=1&url={url}";
            } else if ($(this).is('.n4g')) {
                rel = "http://www.n4g.com/tips.aspx?url={url}&title={title}";
            } else if ($(this).is('.funp')) {
                rel = "http://funp.com/pages/submit/add.php?title={title}&url={url}&via=tools";
            } else if ($(this).is('.care2')) {
                rel = "http://www.care2.com/news/compose?share[link_url]={url}&share[title]={title}";
            } else if ($(this).is('.kirtsy')) {
                rel = "http://www.kirtsy.com/submit.php?url={url}";
            } else if ($(this).is('.wong')) {
                rel = "http://www.mister-wong.com/index.php?action=addurl&bm_url={url}&bm_description={title}";
            } else if ($(this).is('.sphinn')) {
                rel = "http://sphinn.com/index.php?c=post&m=submit&link={url}";
            } else if ($(this).is('.meneame')) {
                rel = "http://meneame.net/submit.php?url={url}";
            } else if ($(this).is('.oknotizie')) {
                rel = "http://oknotizie.alice.it/post?url={url}&title={title}";
            } else if ($(this).is('.aim')) {
                rel = "http://connect.aim.com/share/?url={url}&title={title}";
            } else if ($(this).is('.current')) {
                rel = "http://current.com/clipper.htm?url={url}&title={title}&src=st";
            } else if ($(this).is('.twackle')) {
                rel = "http://www.twackle.com/chicklet?site={url}";
            } else if ($(this).is('.xanga')) {
                rel = "http://www.xanga.com/private/editorx.aspx?t={title}&u={url}&s=";
            } else if ($(this).is('.twine')) {
                rel = "http://www.twine.com/bookmark/basic?u={url}";
            } else if ($(this).is('.ybookmarks')) {
                rel = "http://bookmarks.yahoo.com/toolbar/savebm?opener=tb&u={url}&t={title}";

            } else if ($(this).is('.mailto')) {
                //rel = "mailto://?subject={title}&body=check out this link: {url}";
                rel = "mailto://?subject={title}   [ {url} ]";
            }

            var url = encodeURIComponent(self.location.href);
            var title = encodeURIComponent($("title:first").html());
            rel = rel.replace("{url}", url);
            rel = rel.replace("{title}", title);
            if (rel.substring(4, 0).toLowerCase() == "mail") { self.location.href = rel; } else { window.open(rel); }

            return false;
        });

    }

})(jQuery);
