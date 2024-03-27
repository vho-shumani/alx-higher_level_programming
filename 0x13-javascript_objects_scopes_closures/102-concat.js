#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');
const firstFile = argv[2];
const secondFile = argv[3];
const destinedFile = argv[4];
const text1 = fs.readFileSync(firstFile, 'utf-8');
const text2 = fs.readFileSync(secondFile, 'utf-8');
const mixedText = `${text1}${text2}`;
fs.writeFileSync(destinedFile, mixedText);
