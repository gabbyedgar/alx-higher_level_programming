#!/usr/bin/node
const fs = require('fs');
let args = process.argv.slice(2);
if (args.length < 3) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}
let fa = fs.readFileSync(args[0]);
let fb = fs.readFileSync(args[1]);
fs.writeFileSync(args[2], fa + fb);

