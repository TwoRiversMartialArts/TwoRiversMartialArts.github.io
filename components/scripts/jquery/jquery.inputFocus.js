$(document).ready(function() {
$('input[type="text"],textarea,input[type="password"],input[type="file"],select').addClass("formField");
    $('input[type="text"],textarea,input[type="password"],input[type="file"]').focus(function() {
        $(this).removeClass("formField").addClass("formFieldFocus");
        //if (this.value == this.defaultValue) {
            //this.value = '';
        //}
        if (this.value != this.defaultValue) {
            this.select();
        }
    });
    $('input[type="text"],textarea,input[type="password"],input[type="file"],select').blur(function() {
        $(this).removeClass("formFieldFocus").addClass("formField");
        //if ($.trim(this.value == '')) {
        //    this.value = (this.defaultValue ? this.defaultValue : '');
        //}
    });
});