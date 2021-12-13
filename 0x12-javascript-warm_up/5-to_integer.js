#!/usr/bin/node
const num = Number.parseInt(process.argv[2], 10);
if (!isNaN(num)) {
  console.log(num);
} else {
  console.log('Not a number');
}
