#!/usr/bin/node
let largest = 0;
let secondLargest = 0;

if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 0; i < process.argv.length; i++) {
    const num = Number.parseInt(process.argv[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}
