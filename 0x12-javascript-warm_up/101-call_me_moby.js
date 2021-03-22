#!/usr/bin/node

function callMeMoby (n, func) {
  for (let i = 0; i < n; i++) {
    func();
  }
}
module.exports = {
  callMeMoby: callMeMoby
};
