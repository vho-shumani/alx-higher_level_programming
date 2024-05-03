$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const myList = data.results;
    for (const i in myList) {
      $('#list_movies').append('<li>' + myList[i].title + '</li>');
    }
  });
});
