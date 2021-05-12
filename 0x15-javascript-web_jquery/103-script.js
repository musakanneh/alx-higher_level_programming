function translate() {
    const v = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + v, (data) => {
        $('DIV#hello').html(data.hello);
    });
}

$(function() {
    $('INPUT#btn_translate').click(translate);
});

$(function() {
    $('INPUT#language_code').keypress(function(e) {
        if (e.which === 13) {
            translate();
            return false;
        }
    });
});