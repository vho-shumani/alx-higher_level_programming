#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movieData = JSON.parse(body);
    const urls = movieData.characters;
    async.mapSeries(urls, (characterUrl, callback) => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          callback(err);
        } else {
          const people = JSON.parse(body);
          callback(null, people.name);
        }
      });
    });
  }
});
