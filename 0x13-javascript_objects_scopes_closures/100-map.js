#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((val, ind) => val * ind));
