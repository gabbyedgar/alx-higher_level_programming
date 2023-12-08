#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    let films = JSON.parse(body).results;
    let num = 0;
    for (let film of films) {
      for (let ch of film.characters) {
        if (ch.endsWith('18/')) { num++; break; }
      }
    }
    console.log(num);
  }
});
