#!/usr/bin/node

function addMeMaybe (n, func) {
  n++;
  func(n);
}
module.exports = {
  addMeMaybe: addMeMaybe
};
