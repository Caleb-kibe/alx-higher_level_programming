#!/usr/bin/node

/*
* Creates a class that defines a rectangle
* The width of the rectangle is initialized to w
* The height of the rectangle is initialized to h
* If w or h are equal to 0 or negative, an empty object is created
* Prints the rectangle using the character 'X'
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
