#!/usr/bin/node
// function that converts a number from base 10 to another base
// passed as arguement

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
