#!/usr/bin/node
// print x time the text "C is fun"

const myVar = "C is fun";

if (isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
	console.log(myVar);
    }
}
