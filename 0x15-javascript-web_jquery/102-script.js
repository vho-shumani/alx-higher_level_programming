$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const code = $('#language_code').val();
    console.log(code);
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: code },
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  });
});
