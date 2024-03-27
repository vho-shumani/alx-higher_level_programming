#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  argv.sort((a, b) => a - b);
  console.log(parseInt(argv[argv.length - 2]));
}
