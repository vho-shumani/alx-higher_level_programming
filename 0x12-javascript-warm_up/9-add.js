#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const { argv } = require('node:process');
const firstArg = parseInt(argv[2]);
const secondArg = parseInt(argv[3]);
add(firstArg, secondArg);
