// transition definitions - updated fade is defined here
$.fn.cycle.transitions.fade2 = function($cont, $slides, opts) {
    $slides.not(':eq(' + opts.currSlide + ')').css({ display: 'block', 'opacity': 1 });
    opts.before.push(function(curr, next, opts, w, h, rev) {
        $(curr).css('zIndex', opts.slideCount + (!rev === true ? 1 : 0));
        $(next).css('zIndex', opts.slideCount + (!rev === true ? 0 : 1));
    });
    opts.animIn = { opacity: 1 };
    opts.animOut = { opacity: 0 };
    opts.cssBefore = { opacity: 1, display: 'block' };
    opts.cssAfter = { zIndex: 0 };
};
