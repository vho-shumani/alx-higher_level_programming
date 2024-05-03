$('document').ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.mylist li:last').remove();
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.mylist').empty();
  });
});
