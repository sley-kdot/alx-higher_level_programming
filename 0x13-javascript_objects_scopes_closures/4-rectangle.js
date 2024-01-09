#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0)) {
      return this.Rectangle;
    }
    if ((w === undefined) || (h === undefined)) {
      return this.Rectangle;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let str = '';
      for (let j = 1; j <= this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    let temp;
    temp = this.width
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
