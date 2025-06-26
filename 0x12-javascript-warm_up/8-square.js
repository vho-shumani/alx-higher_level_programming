#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
  for (let i = 1; i <= arg; i++) {
    console.log('X'.repeat(arg));
  }
} else {
  console.log('Missing size');
}
