#!/usr/bin/node

/*
* prints a sqaure
* The first argument is the size of the sqaure
* If the first argument cannot be converted to an integer
* print 'missing size'
*/

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
