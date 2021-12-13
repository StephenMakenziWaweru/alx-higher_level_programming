#!/usr/bin/node
const size = Number.parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let sq = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      sq += 'X';
    }
    if (i < size - 1) {
      sq += '\n';
    }
  }
  console.log(sq);
}
