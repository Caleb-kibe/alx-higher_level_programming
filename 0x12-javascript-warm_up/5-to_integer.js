#!/usr/bin/node

/*
* Checks if an argument is a number
* Prints the number if the argument is a number
* Prints "Not a number" if argument is not a number
*/

const num = parseInt(process.argv[2]);

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
