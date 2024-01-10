#!/usr/bin/node
const arr = require('./100-data');

const mapArr = arr.list.map((x, idx) => x * idx);

console.log(arr.list);
console.log(mapArr);
