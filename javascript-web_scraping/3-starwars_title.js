#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const website = 'https://swapi-api.hbtn.io/api/films/' + url;

request(website, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonReturn = JSON.parse(body);
    console.log(jsonReturn.title);
  }
});
