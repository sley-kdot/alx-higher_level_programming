#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
