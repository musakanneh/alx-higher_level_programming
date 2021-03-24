#!/usr/bin/node

let c = -1;
exports.logMe = function (item) {
  function printLog (item) {
    c++;
    console.log(`${c}: ${item}`);
  }
  return printLog(item);
};
