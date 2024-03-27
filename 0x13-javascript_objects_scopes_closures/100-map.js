#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map(multiplier);
function multiplier (element, index, array) {
  return element * index;
}
console.log(list);
console.log(newList);
