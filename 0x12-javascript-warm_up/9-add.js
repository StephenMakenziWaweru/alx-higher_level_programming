#!/usr/bin/node
const a = Number.parseInt(process.argv[2], 10);
const b = Number.parseInt(process.argv[3], 10);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(a, b);
