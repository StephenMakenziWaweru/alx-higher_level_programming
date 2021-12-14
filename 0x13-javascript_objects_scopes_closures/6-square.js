#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let rec = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          rec += 'C';
        } else {
          rec += 'X';
        }
      }
      rec += '\n';
    }
    process.stdout.write(rec)
  }
}

module.exports = Square;
