#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (error, response, body) => {
  if (error) console.log(error);

  const movie = JSON.parse(body);
  for (let index = 0; index < movie.characters.length; index++) {
    const characterUrl = movie.characters[index];

    request(characterUrl, (err, res, bdy) => {
      if (err) console.log(err);
      const character = JSON.parse(bdy);
      console.log(character.name);
    });
  }
});
