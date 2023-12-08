$('#add_item').click(function () {
  $(this).nextAll('ul.my_list').append('<li>Item</li>');
});
