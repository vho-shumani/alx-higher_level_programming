#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};
    todos.forEach(todo => {
      if (todo.completed) {
        completedTasks[todo.userId] = 0;
      }
    });
    todos.forEach(todo => {
      if (todo.completed) {
        completedTasks[todo.userId]++;
      }
    }
    );
    console.log(completedTasks);
  }
});
