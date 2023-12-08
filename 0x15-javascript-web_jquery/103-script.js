$(function () {
  $('input#btn_search').click(function () {
    let city = $('#city_search').val();
    let windurl = 'https://query.yahooapis.com/v1/public/yql?' +
      'q=select%20wind%20from%20weather.forecast%20where%20' +
      'woeid%20in%20(select%20woeid%20from%20geo.places(1)%' +
      `20where%20text%3D%22${city}%22)&format=json`;
    $.getJSON(windurl, data => {
      let results = data.query.results;
      $('#wind_speed').text(results === null ? 0 : results.channel.wind.speed);
    });
  });
  $('#city_search').keypress(e => {
    if (e.which === 13) {
      $('#btn_search').click();
    }
  });
});
