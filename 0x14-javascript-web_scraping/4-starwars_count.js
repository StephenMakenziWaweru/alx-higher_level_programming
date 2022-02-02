#!/usr/bin/node
// prints the number of movies where "Wedge Antilles' is present
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) throw new Error(error);
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    const res = film.characters.includes("https://swapi-api.hbtn.io/api/people/18/");
    count += (res ? 1 : 0);
  });
  console.log(count);
});
