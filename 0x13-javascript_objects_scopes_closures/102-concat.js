#!/usr/bin/node
// concats 2 files

const fs = require('fs');

const datafila = fs.readFileSync(process.argv[2], 'utf8');
const datafilb = fs.readFileSync(process.argv[3], 'utf8');
const content = datafila + datafilb;
fs.writeFile(process.argv[4], content, err => {
  if (err) {
    console.error(err);
  }
});
