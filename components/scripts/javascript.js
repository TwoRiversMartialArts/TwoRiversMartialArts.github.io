function printArticle() {
    if (window.print) {
        window.print();
    } else if (agt.indexOf("mac") != -1) {
        alert("Press 'Cmd+p' on your keyboard to print article.");
    } else {
        alert("Press 'Ctrl+p' on your keyboard to print article.")
    }
}

function displaySample(gohere) {
    //1024×768
    window.open(gohere, "window1", config = "width=1010,height=650,resizable=yes,toolbar=no,scrollbars=yes,menubar=no,location=no,top=50,left=50");
}

function addressBook(gohere) {
    window.open(gohere, "window1", config = "width=660,height=640,resizable=no,toolbar=no,scrollbars=no,menubar=no,location=no,top=50,left=50");
}

function commentsListing(gohere) {
    window.open(gohere, "window1", config = "width=535,height=640,resizable=yes,toolbar=no,scrollbars=yes,menubar=no,location=no,top=50,left=50");
}

function performSearch(currPage, phrase) {
    window.location.href = (currPage + "?srch=" + phrase);
    return false;
}


function openFileBrowse(gohere) {
    fileBrowse = window.open(gohere, "FileBrowser", config = "width=760,height=350,resizable=yes,toolbar=no,scrollbars=yes,menubar=no,location=no,top=" + (screen.height - (screen.height * .75)) / 2 + ",left=" + (screen.width - (screen.width * .75)) / 2 + "");
}

function closeDep() {
    if (fileBrowse && fileBrowse.open && !fileBrowse.closed) fileBrowse.close();
}

function SetUrl(url) {
    try {
        document.getElementById(valueTarget).value = url;
        closeDep();
        __doPostBack(valueTarget);
    } catch (Error) {
    }
}



//function openFileBrowse(gohere) {
//    fileBrowse = window.open(gohere, "privacy", config = "width=" + screen.width * .75 + ",height=" + screen.height * .75 + ",resizable=yes,toolbar=yes,scrollbars=yes,menubar=yes,location=yes,top=" + (screen.height - (screen.height * .75)) / 2 + ",left=" + (screen.width - (screen.width * .75)) / 2 + "");
//}

//function closeDep() {
//    if (fileBrowse && fileBrowse.open && !fileBrowse.closed) fileBrowse.close();
//}

//function SetUrl(url) {
//    try { 
//        document.getElementById(valueTarget).value = url;
//        closeDep();
//        __doPostBack(valueTarget);
//    } catch (Error) {
//        document.getElementById(valueTargetAlbum).value = url;
//        closeDep();
//        __doPostBack(valueTargetAlbum);
//    }
//}


function setSelectionRange(input, selectionStart, selectionEnd) {
    if (input.setSelectionRange) {
        input.focus();
        input.setSelectionRange(selectionStart, selectionEnd);
    } else if (input.createTextRange) {
        var range = input.createTextRange();
        range.collapse(true);
        range.moveEnd('character', selectionEnd);
        range.moveStart('character', selectionStart);
        range.select();
    }
}

function setCaretToEnd(input) {
    setSelectionRange(input, input.value.length, input.value.length);
}

function removeHTMLTags(elementId) {
    if (document.getElementById && document.getElementById(elementId)) {
        var strInputCode = document.getElementById(elementId).innerText;
        strInputCode = strInputCode.replace(/&(lt|gt);/g, function(strMatch, p1) {
            return (p1 == "lt") ? "<" : ">";
        });
        var strTagStrippedText = strInputCode.replace(/<\/?[^>]+(>|$)/g, "");
        document.getElementById(elementId).innerText = strTagStrippedText;
    }
}

function MakeStringXMLCompliant(elementId) {
    if (document.getElementById && document.getElementById(elementId)) {
        var strInputCode = document.getElementById(elementId).value;
        var strTagStrippedText = strInputCode.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        document.getElementById(elementId).value = strTagStrippedText;
    }
}



//Updated accordian script 9/9/10 by KSG
$(document).ready(function() {
    $('ul.accordian> li div').hide();
    $('ul.accordian> li div div').show();
    $('ul.accordian> li span').addClass('offTitle');
    $('ul.accordian> li div').addClass('offContent');

    //Added 9/9/10 to open the first record
    //$('ul.accordian div:first').show();

    $('ul.accordian> li span').click(function() {
        var pid = "";
        try { pid = $(this).closest("ul.accordian").attr("id") } catch (err) { }
        $('ul#' + pid + '.accordian> li span').removeClass('onTitle');
        $('ul#' + pid + '.accordian> li span').removeClass('offTitle');
        $('ul#' + pid + '.accordian> li span').addClass('offTitle');
        if ($(this).next('div').is(':visible')) {
            $(this).removeClass('onTitle');
            $(this).addClass('offTitle');
        } else {
            $(this).removeClass('offTitle');
            $(this).addClass('onTitle');
        }
        $('ul#' + pid + '.accordian> li div').removeClass('onContent');
        $('ul#' + pid + '.accordian> li div').removeClass('offContent');
        $('ul#' + pid + '.accordian> li div').addClass('offContent');
        $('ul#' + pid + '.accordian> li div:visible').removeClass('offContent');
        $('ul#' + pid + '.accordian> li div:visible').addClass('onContent');
        $('ul#' + pid + '.accordian> li div div').show();
        $('ul#' + pid + '.accordian> li div ul.accordian li div').hide();
        $('ul#' + pid + '.accordian> li div:visible').slideUp('fast');
        $(this).next('div:hidden').slideToggle('fast');
    });
});


