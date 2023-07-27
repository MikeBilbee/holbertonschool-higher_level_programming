#!/usr/bin/node

const firstArg = (...args) => {
  const arrayLength = args.length;
  if (arrayLength === 0) {
    console.log('No argument');
  } else if (arrayLength === 1) {
    console.log(args[0]);
  } else {
    console.log('Too many arguments');
  }
};

firstArg();
