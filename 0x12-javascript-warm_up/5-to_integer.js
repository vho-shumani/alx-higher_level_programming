#!/usr/bin/node

const arg = parseInt(process.argv[2]);

(arg) ? console.log(`My number: ${arg}`) : console.log('Not a number');
