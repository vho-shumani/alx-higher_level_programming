#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = parseInt(argv[2]);
if (!isNaN(firstArg)) {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
