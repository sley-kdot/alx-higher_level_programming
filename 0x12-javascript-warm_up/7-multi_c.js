#!/usr/bin/node
const args = process.argv;

const number = parseInt(args[2]);
let i = 1;

if (args.length === 2) {
  console.log('Missing number of occurences');
} else {
  while (i <= number) {
    console.log('C is fun');
    i++;
  }
}
