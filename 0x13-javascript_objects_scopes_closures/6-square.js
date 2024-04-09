// Creates a class Square that inherits from class Square of 5-square.js
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row = row + 'X';
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row = row + 'c';
        }
        console.log(row);
      }
    }
  }
};
