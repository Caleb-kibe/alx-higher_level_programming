#!/usr/bin/node
// Creates a class Square that inherits from class Square of 5-square.js
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'x';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row = row + c;
      }
      console.log(row);
    }
  }
};
