#!/usr/bin/node
const request = require('request');
const requests = require('sync-request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body);
    films.characters.forEach( characterUrl => {
	const characterRes = requests('GET', characterUrl);
	const character = JSON.parse(characterRes.getBody());
	console.log(character.name);
    });
  }
});
