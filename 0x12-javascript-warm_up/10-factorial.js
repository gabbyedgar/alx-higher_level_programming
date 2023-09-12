#!/usr/bin/node
function fact (n) {
  if (isNaN(n) || n <= 1) return 1;
  return n * fact(n - 1);
}
let n = parseInt(process.argv[2]);
console.log(fact(n));
