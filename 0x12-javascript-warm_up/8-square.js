#!/usr/bin/node
const args = process.argv;

const number = parseInt(args[2]);
let str = '';
if (isNaN(parseInt(number))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= number; i++) {
    for (let j = 1; j <= number; j++) {
      str += 'X';
    }
    if (i < number) {
      str += '\n';
    }
  }
  console.log(str);
}
