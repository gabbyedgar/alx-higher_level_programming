$(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', data => {
    let list = $('ul#list_movies');
    $.each(data.results, (idx, film) => {
      list.append('<li>' + film.title + '</li>');
    });
  });
});
