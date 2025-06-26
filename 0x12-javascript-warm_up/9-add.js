#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const firstNum = parseInt(process.argv[2]);
const secondNum = parseInt(process.argv[3]);

add(firstNum, secondNum);
