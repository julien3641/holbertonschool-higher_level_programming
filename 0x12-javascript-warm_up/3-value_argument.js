#!/usr/bin/node
// prints the first args passed else no argument
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
