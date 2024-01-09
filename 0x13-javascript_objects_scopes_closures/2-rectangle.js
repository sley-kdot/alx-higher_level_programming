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
}
module.exports = Rectangle;
