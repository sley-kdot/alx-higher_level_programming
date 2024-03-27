#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileName = args[2];
const text = args[3];

fs.writeFile(fileName, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(text);
  }
});
