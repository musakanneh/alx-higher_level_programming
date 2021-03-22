#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.slice(2);
  let secondElement = Number.MIN_VALUE;
  let maxValue = Number.MAX_VALUE;

  arr.forEach(function (element) {
    element = parseInt(element);
    if (element > maxValue) {
      secondElement = maxValue;
      maxValue = element;
    } else if (secondElement < element && maxValue > element) {
      secondElement = element;
    }
  });
  console.log(secondElement);
}
