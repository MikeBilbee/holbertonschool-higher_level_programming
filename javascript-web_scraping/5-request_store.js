#!/usr/bin/node

const fileServer = require('fs');

const request = require('request');

const url = process.argv[2];

const file = process.argv[3];

request(url).pipe(fileServer.createWriteStream(file));
