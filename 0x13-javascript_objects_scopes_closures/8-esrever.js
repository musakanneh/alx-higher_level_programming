#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (arr, last) {
    return (arr = arr.concat(last));
  }, []);
};
