#!/usr/bin/node
// script that print a square

const myVar = 'X';

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < (parseInt(process.argv[2])); i++) {
      console.log(myVar.repeat(parseInt(process.argv[2])));
  }
}
