#!/usr/bin/node

// Counts the number of arguments already printed and prints the current argument
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
