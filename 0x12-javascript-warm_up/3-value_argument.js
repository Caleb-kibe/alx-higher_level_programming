#!/usr/bin/node

/*
 * Prints the first argument passed to it
 * Prints "No arguments" if no arguments are passed
*/

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
