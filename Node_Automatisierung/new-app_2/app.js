const express = require('express');

// express App

const app = express();

// listen for requests
app.listen(3000, () => console.log('Listening on port 3000...'));

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', (req,res) => {
  // res.send('<p>Home</p>');
  res.sendFile('./views/index.html', {root: __dirname});
});
app.get('/about', (req,res) => {
  res.send('<p>about</p>');
});

// Own API - call
app.get('/posts', (req,res) => {
  let restData = {id: 10, name: "Heinz"};
  res.send(JSON.stringify({id: 10, name: 12}));
});

// redirect
app.get('/', (req,res) => {
  res.redirect('/about');
});

// 404 page (must be ont the bottom, because node 'walks' from top to bottom...)
app.use((req,res) => {
  res.send('<p>OOps - 404 not found.</p>');
});