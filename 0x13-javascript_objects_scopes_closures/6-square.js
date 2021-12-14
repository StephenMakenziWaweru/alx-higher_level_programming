#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let rec = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          rec += 'C';
        } else {
          rec += 'X';
        }
      }
      if (i < this.height - 1) {
        rec += '\n';
      }
    }
    console.log(rec);
  }
}

module.exports = Square;
