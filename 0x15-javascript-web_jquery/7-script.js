window.fetch('https://swapi.co/api/people/5/?format=json')
    .then((res) => res.json())
    .then(function(data) {
        $('DIV#character').text(data.name);
    });