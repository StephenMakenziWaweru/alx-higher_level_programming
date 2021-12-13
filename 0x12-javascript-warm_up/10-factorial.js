#!/usr/bin/node
const n = Number.parseInt(process.argv[2], 10);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(n));
