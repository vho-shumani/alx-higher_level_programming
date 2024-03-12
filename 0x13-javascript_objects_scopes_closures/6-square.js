#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c == null) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
        }
    }   
  }
} module.exports = Square;
