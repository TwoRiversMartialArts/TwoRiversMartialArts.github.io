
var ar = new Array(33, 34, 35, 36, 37, 38, 39, 40);

function checkKey(e) {
    if ($.inArray(key, ar)) {
        e.preventDefault();
        return false;
    }
    return true;
}

if ($.browser.mozilla) {
    $(document).keypress(checkKey);
} else {
    $(document).keydown(checkKey);
}

