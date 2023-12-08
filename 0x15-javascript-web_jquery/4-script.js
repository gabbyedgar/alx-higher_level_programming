$(function () {
  $('#toggle_header').addClass('red');
});

$('#toggle_header').click(function () {
  $(this).toggleClass('red');
  $(this).toggleClass('green');
});
