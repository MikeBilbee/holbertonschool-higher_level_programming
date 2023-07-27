#!/usr/bin/node

const firstArg = (...args) => {
  if (args.length === 0) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
};

firstArg();
