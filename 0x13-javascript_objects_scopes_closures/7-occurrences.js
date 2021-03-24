#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, val) => {
    if (val === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
