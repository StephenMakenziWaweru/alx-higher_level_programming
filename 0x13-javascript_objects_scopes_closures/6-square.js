#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
