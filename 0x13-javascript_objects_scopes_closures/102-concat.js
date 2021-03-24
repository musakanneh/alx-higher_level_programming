#!/usr/bin/node

const cmd = `cat ${process.argv[2]} ${process.argv[3]} > ${process.argv[4]}`;
require('child_process').execSync(cmd).toString('UTF-8');
