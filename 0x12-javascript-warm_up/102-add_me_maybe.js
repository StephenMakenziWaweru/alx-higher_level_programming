#!/usr/bin/node
module.exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
