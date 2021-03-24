#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = 'X'.repeat(this.width) + '\n';
    a = a.repeat(this.height);
    console.log(a.slice(0, -1));
  }
};
