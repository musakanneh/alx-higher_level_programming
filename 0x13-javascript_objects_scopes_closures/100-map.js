#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const newList = list.map((v, i) => v * i);
console.log(newList);
