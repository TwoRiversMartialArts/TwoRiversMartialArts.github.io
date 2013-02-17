$(window).load(function() {
    var $ads;
    $('div[id^="adsref-"]').each(function() {
        $ads = $('#ads-' + this.id.substr(7)).empty();
        $('ins:first', this).appendTo($ads);
        //$(this).contents().appendTo($ads);
    });
});
