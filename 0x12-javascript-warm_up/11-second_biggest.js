#!/usr/bin/node
// script that searches the second biggest integer in the list arguments

if (process.argv.length <=3) {
    console.log(0);
} else {
    const arr = [];
    for (let i = 2; i < process.argv.length; i++) {
	arr[i] = parseInt(process.argv[i]);
    }
    arr.sort();
    console.log(1);
}
