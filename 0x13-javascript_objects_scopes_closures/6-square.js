#!/usr/bin/node

const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  charPrint (char) {
    const c = char || 'X';
    let a = c.repeat(this.width) + '\n';
    a = a.repeat(this.height);
    console.log(a.slice(0, -1));
  }
};
