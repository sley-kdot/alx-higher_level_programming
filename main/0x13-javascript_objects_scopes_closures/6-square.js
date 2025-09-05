#!/usr/bin/node
const SquareModified = require('./5-square');

class Square extends SquareModified {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      let str = '';
      for (let j = 1; j <= this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
