#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const arg = parseInt(process.argv[2]);
const result = factorial(arg);
console.log(result);
