#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
let characters;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) throw new Error(error);
  characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request(character, (error, response, body) => {
      console.log(JSON.parse(body).name);
    });
  });
});
