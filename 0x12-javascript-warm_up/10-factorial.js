#!/usr/bin/node

/**
 * a script that computes and prints a factorial
 */
function factorial (num) {
  if (num === 1 || num === 1 || isNaN(num)) {
    return (1);
  }
  return (factorial(num - 1) * num);
}
console.log(factorial(parseInt(process.argv[2])));
