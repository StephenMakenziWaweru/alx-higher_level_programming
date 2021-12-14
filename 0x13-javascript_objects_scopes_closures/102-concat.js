#!/usr/bin/node
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2], 'utf-8');
const fileB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], fileA + fileB, 'utf-8');
