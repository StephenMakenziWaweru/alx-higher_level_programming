#!/usr/bin/node
// prints the number of movies where "Wedge Antilles' is present
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) throw new Error(error);
  let count = 0;
  JSON.parse(body).results.forEach(film => {
    film.characters.forEach(character => {
      const res = character.includes('/18/');
      count += (res ? 1 : 0);
    });
  });
  console.log(count);
});
