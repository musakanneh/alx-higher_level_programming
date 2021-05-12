window.fetch('https://fourtonfish.com/hellosalut/?lang=fr')
    .then((res) => res.json())
    .then(function(data) {
        $('DIV#hello').text(data.hello);
    });