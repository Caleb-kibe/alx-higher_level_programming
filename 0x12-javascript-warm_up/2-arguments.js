#!/usr/bin/node

/*
 * Prints a message depending on the number of arguments passed
 * Prints "No argument" if no argument is passed
 * Prints "Argument found" if one argument is passed
 * Prints "Arguments found" if more than one argument is passed
 */

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
