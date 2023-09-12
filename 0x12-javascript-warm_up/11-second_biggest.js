#!/usr/bin/node
let args = process.argv.slice(2).map((item) => parseInt(item));
if (args.length <= 1) console.log(0);
else {
  let max = args[0];
  let second = args[1];
  for (let i = 1; i < args.length; i++) {
    if (args[i] > max) {
      second = max;
      max = args[i];
    } else if (args[i] > second) {
      second = args[i];
    }
  }
  console.log(second);
}

