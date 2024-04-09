#!/usr/bin/node

/*
* Creates a class that defines a rectangle
* The width of the rectangle is initialized to w
* The height of the rectangle is initialized to h
* If w or h are equal to 0 or negative, an empty object is created
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints the rectangle using the character 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // Exchages the width and height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Multiplies the width and height of the rectangle by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
