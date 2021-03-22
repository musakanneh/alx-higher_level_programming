#!/usr/bin/node

const userArgs = parseInt(process.argv[2]);
let argsCount = 0;

if (isNaN(userArgs)) {
  console.log('Missing number of occurrences');
}
while (argsCount < userArgs) {
  console.log('C is fun');
  argsCount++;
}
