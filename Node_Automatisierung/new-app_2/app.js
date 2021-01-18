const express = require('express');
const mongoose = require('mongoose');
const Measuring = require('./Modules/database.schema');

// express App with mongoose
const app = express();

// listen for requests
app.listen(3000, () => console.log('Listening on port 3000...'));

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, x-token");
  next();
});
app.use(express.json());

app.get('/', (req,res) => {
  // res.send('<p>Home</p>');
  res.sendFile('./views/index.html', {root: __dirname});
});
app.get('/about', (req,res) => {
  res.send('<p>about</p>');
});

// Own API - call
app.get('/posts', (req,res) => {
  res.send({id: 10, name: "Roberto Carlos"});
    //JSON.stringify({id: 10, name: 12});
});

//DB-Test
app.get('/measuringdata', async (req,res) => {
  try {
      const newMeasuringData = await Measuring.find();
      res.send(newMeasuringData);
  } catch (err){
      res.status(500).json({message: err.message});
  }
});

app.post('/postmeasuringdata', async (req,res) => {
    const entryData = new Measuring({
        name: req.body.name,
        description: req.body.description,
    })
    try {
        const newMeasuringData = await entryData.save();
        res.status(201).json(newMeasuringData);
    } catch (err){
        res.status(400).json({message: err.message});
    }
});



// redirect
app.get('/', (req,res) => {
  res.redirect('/about');
});

// 404 page (must be ont the bottom, because node 'walks' from top to bottom...)
app.use((req,res) => {
  res.send('<p>OOps - 404 not found.</p>');
});