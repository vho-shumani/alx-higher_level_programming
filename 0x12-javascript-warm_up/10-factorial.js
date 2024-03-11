#!/usr/bin/node
function factorial(a){
  if (a == 1 || isNaN(a)){
    return 1;
  }
  a *= factorial(a - 1);
  return a;
}
const { argv } = require('node:process');
const firstArg = parseInt(argv[2]);
console.log(factorial(firstArg));
