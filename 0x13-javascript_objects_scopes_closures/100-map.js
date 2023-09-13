#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
console.log(list.map((element, index) => element * index));

