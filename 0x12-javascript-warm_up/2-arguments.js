#!/usr/bin/node
const { argv } = require('node:process');
const lengthArgv = argv.length;
if (lengthArgv === 2) {
  console.log('No argument');
} else if (lengthArgv === 3) {
  console.log('Argument found');
} else if (lengthArgv > 3) {
  console.log('Arguments found');
}
