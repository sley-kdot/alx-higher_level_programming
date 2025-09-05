#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv;
const url = args[2];
const filePath = args[3];

request(url, (error, response, body) => {
  if (error) console.log(error);

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) console.log(err);
  });
});
