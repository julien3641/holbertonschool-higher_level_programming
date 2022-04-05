#!/usr/bin/node
// function that prints the number of arguments
// already printed and the new argument value.

exports.logMe = (function (item) {
  let count = -1;
  return function (item) {
    count++;
    console.log(count + ': ' + item);
  };
})();
