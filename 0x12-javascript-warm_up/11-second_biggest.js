#!/usr/bin/node
const args = process.argv;

const size = args.length;
let firstLargest = parseInt(args[2]);
let secondLargest = parseInt(args[3]);

if (size <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < size; i++) {
    if (parseInt(args[i]) > firstLargest) {
      firstLargest = parseInt(args[i]);
    } else if ((parseInt(args[i]) > secondLargest) && (secondLargest !== firstLargest)) {
      secondLargest = parseInt(args[i]);
    }
  }
  console.log(secondLargest);
}
