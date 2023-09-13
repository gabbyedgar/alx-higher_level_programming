#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || searchElement === undefined) return 0;
  let n = 0;
  list.forEach((element) => { if (element === searchElement) n++; });
  return n;
};

