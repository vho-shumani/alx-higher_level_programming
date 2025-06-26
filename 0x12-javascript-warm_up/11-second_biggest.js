#!/usr/bin/node

const arr = process.argv.slice(2).sort((a, b) => a - b);
const lenArray = arr.length;

(lenArray <= 1) ? console.log(0) : console.log(arr[lenArray - 2]);
