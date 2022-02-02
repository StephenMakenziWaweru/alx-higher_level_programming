#!/usr/bin/node
// computes numner of tasks completed by user id
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) throw new Error(error);
  const tasks = JSON.parse(body);
  const users = {};
  tasks.forEach(task => {
    if (task.completed) {
      if (!users[task.userId.toString()]) {
        users[task.userId.toString()] = 0;
      }
      users[task.userId.toString()] += 1;
    }
  });
  console.log(users);
});
