#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[i] = list[j];
    j++;
  }
  return reversedList;
};
