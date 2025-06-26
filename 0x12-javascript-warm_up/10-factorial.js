#!/usr/bin/node

const arg = parseInt(process.argv[2]);
(!arg) ? console.log(1) : console.log(factorial(arg));

function factorial (n) {
  if (n <= 1) {
    return 1;
  }

  return (factorial(n - 1) * n);
}
