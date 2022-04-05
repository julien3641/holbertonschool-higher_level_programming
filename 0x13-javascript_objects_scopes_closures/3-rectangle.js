#!/usr/bin/node
// Class that defines a rectangle with width and height

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < (parseInt(this.height)); i++) {
      console.log('X'.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Rectangle;
