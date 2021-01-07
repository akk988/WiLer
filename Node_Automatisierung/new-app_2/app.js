const express = require('express');

// express App

const app = express();

// listen for requests
app.listen(3000);

app.get('/', (req,res) => {
  // res.send('<p>Home</p>');
  res.sendFile('./views/index.html', {root: __dirname});
});
app.get('/about', (req,res) => {
  res.send('<p>about</p>');
});

// redirect
app.get('/', (req,res) => {
  res.redirect('/about');
});

// 404 page (must be ont the bottom, because node 'walks' from top to bottom...)
app.use((req,res) => {
  res.send('<p>OOps - 404 not found.</p>');
});