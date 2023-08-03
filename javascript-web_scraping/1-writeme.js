#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL to request as an argument.');
} else {
  request.get(url, (error, response) => {
    if (error) {
      console.error('Error occurred:', error);
    } else {
      console.log('code:', response.statusCode);
    }
  });
}
