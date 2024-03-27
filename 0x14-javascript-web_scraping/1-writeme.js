#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileName = args[2];
const text = args[3];

if (args.length < 4) {
  console.log('USAGE: ./1-writeme.js file_name file_content');
  process.exit(1);
}

fs.writeFile(fileName, text, (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(text);
  }
});
