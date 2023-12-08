$(function () {
  $.getJSON('https://swapi.co/api/people/5/?format=json', data => {
    $('#character').text(data.name);
  });
});
