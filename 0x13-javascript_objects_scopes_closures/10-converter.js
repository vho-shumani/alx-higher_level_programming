#!/usr/bin/node
exports.converter = function (base) {
  return function baseConverter (num) {
    return num.toString(base);
  };
};
