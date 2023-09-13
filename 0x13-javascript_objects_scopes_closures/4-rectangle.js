#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

