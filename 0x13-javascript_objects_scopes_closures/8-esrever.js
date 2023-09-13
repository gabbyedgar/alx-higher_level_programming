#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined) return [];
  let reversed = [];
  for (let l = list.length - 1; l >= 0; l--) {
    reversed.push(list[l]);
  }
  return reversed;
};

