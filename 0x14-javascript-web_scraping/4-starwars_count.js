#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body);
    const wedges = movies.results.filter(movies => {
      return movies.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(wedges.length);
  }
});
