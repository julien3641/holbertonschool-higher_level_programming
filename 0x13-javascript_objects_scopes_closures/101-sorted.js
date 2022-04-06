#!/usr/bin/node
// script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence
const dict = require('./101-data.js').dict;

const newdict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newdict[value] !== undefined) {
    newdict[value].push(key);
  } else {
    newdict[value] = [key];
  }
}
console.log(newdict);
