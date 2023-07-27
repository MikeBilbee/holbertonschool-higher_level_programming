#!/usr/bin/node

const findSecondBiggest = (args) => {
  if (args.length <= 1) {
    return 0;
  }

  let largest = parseInt(args[2]);
  let secondLargest = parseInt(args[3]);

  if (largest < secondLargest) {
    [largest, secondLargest] = [secondLargest, largest];
  }

  for (let i = 4; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
};

const args = process.argv;
const result = findSecondBiggest(args);
console.log(result);
