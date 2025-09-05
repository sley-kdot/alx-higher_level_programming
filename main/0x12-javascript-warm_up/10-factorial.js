#!/usr/bin/node
const args = process.argv;

const number = parseInt(args[2]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(number));
