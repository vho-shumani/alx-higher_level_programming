#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = parseInt(argv[2]);
if (!isNaN(firstArg)) {
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
} else {
  console.log('Missing size');
}
