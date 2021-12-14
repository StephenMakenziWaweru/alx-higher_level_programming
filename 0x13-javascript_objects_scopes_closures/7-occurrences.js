#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurrence += 1;
    }
  }
  return occurrence;
};
