#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (!Number.isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
