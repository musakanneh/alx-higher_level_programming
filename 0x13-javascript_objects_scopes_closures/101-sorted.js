#!/usr/bin/node

const dict = require('./101-data').dict;

const entries = Object.entries(dict);
const newDict = {};
for (const [key, value] of entries) {
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
