window.fetch('https://swapi.co/api/films/?format=json')
    .then((res) => res.json())
    .then(function(data) {
        data = data.results;
        for (const obj of data) {
            $('UL#list_movies').append(`<li>${obj.title}</li>`);
        }
    });