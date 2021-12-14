#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      if (i < this.height - 1) {
        rec += '\n';
      }
    }
    console.log(rec);
  }
}
module.exports = Rectangle;
