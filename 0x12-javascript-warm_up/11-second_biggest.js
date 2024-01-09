#!/usr/bin/node
const args = process.argv;

const size = args.length;
let firstLargest = parseInt(args[2]);
let secondLargest = parseInt(args[3]);

if (size <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < size; i++) {
    const currentNum = parseInt(args[i]);

    if (currentNum > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = currentNum;
    } else if ((currentNum > secondLargest) && (currentNum < firstLargest)) {
      secondLargest = currentNum;
    }
  }
  console.log(secondLargest);
}
