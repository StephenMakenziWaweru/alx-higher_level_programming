#!/usr/bin/node
let largest = 0;
let second_largest = 0;
let prev = 0;

if (process.argv.length < 4) {
  console.log(0);
} else {
  for (i = 0; i < process.argv.length; i++) {
    num = Number.parseInt(process.argv[i]);
    if (num > largest) {
      second_largest = largest;
      largest = num;
    } else if (num > second_largest && num < largest) {
	    second_largest = num;
    }
  }
  console.log(second_largest);
}
