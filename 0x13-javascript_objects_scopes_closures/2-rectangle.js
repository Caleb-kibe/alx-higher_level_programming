#!/usr/bin/node

/*
* Creates a class that defines a rectangle
* The width of the rectangle is initialized to w
* The height of the rectangle is initialized to h
* If w or h are equal to 0 or negative, an empty object is created
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
};
