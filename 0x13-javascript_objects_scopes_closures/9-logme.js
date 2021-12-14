#!/usr/bin/node

let noOfItemsPrinted = 0;
exports.logMe = function (item) {
  console.log(`${noOfItemsPrinted}: ${item}`);
  noOfItemsPrinted += 1;
};
