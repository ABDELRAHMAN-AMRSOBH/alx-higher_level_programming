#!/usr/bin/node
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 1; j <= this.width; j++) {
        result += c;
      }
      console.log(result);
    }
  }
}

module.exports = Square;
