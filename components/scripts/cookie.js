

function readCookie(c_name) {
    if (getCookie(c_name) == "") {
        trackStat(c_name);
    }
    return getCookie(c_name)
}

function trackStat(c_name) {
    var now = new Date()
    var tzo = (now.getTimezoneOffset() / 60) * (-1);
    var hist = history.length;
    var scrH = screen.height;
    var scrW = screen.width;
    var scrC = screen.colorDepth;
    var scrRef = "";
    var userA = window.navigator.userAgent;

    if (document.referrer && document.referrer != "") {
        scrRef = document.referrer;
    }

    setCookie(c_name, "tzo:" + tzo + "|scrH:" + scrH + "|scrW:" + scrW + "|scrC:" + scrC + "|hist:" + hist + "|scrRef:" + scrRef + "|uAgent:" + userA, 1);
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=")
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1
            c_end = document.cookie.indexOf(";", c_start)
            if (c_end == -1)
                c_end = document.cookie.length
            return unescape(document.cookie.substring(c_start, c_end))
        }
    }
    return ""
}

function setCookie(c_name, value, expiredays) {
    var today = new Date();
    var expire = new Date();
    if (expiredays == null || expiredays == 0) expiredays = 1;
    expire.setTime(today.getTime() + 3600000 * 24 * expiredays);

//    c_name = c_name.replace(/[^0-9a-zA-Z]/, "");
//    value = value.replace(/[^0-9a-zA-Z]/, "");
//    
    document.cookie = c_name + "=" + escape(value) + ";expires=" + expire.toGMTString();
}
