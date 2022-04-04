#!/usr/bin/node
// script that searches the second biggest integer in the list arguments

let biggest = process.argv[2];
let nextbiggest = process.argv[2];

if (process.argv.length <= 2) {
    console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      nextbiggest = biggest;
      biggest = process.argv[i];
    } else if (process.argv[i] > nextbiggest && process.argv[î] !== biggest) {
      nextbiggest = process.argv[i];
    }
  }
}
console.log(nextbiggest);
