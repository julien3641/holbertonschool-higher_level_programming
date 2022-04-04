#!/usr/bin/node
// script that searches the second biggest integer in the list arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.sort();
  console.log(args.reverse()[1]);
}
