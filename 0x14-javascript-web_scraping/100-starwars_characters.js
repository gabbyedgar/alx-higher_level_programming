#!/usr/bin/node
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], (err, resp, body) => {
  if (err) console.log(err);
  else if (resp.statusCode === 200) {
    let film = JSON.parse(body);
    for (let ch of film.characters) {
      request.get(ch, (err, resp, body) => {
        if (err) console.log(err);
        else if (resp.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
