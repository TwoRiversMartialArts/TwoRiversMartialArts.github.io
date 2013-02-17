$(document).ready(function() {
    $('#pageselection').hide();
    $('#clickshow').click(function() {
        if ($('#pageselection').is(':hidden')) {
            $('#pageselection').slideDown('slow');
        } else {
            $('#pageselection').slideUp('slow');
        }
    });

    $('a[href=#top]').click(function() {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
        return false;
    });

});
