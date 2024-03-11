#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = argv[2];
const secondArg = argv[3];
console.log(`${firstArg} is ${secondArg}`);
