$('DIV#toggle_header').addClass('green');
$(function() {
    $('DIV#toggle_header').click(function(e) {
        $(this).toggleClass('red green');
        e.preventDefault();
    });
});