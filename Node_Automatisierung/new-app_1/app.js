// Integrade Own Moduels
// const add = require('./Modules/module_one');
// add();

// -----------------------------------------------------------

// Parsing Strings
// const path = require('path');
// var pathObj = path.parse(__filename);
// console.log('Path Object: ' + pathObj);

// -----------------------------------------------------------

// Working with the OS
// const os = require('os');
// var totalMemory = os.totalmem();
// var freeMemory = os.freemem();
// console.log('Total Memory: ' + totalMemory);
// console.log('Free Memory: ' + freeMemory);

// -----------------------------------------------------------

// Working with files
// const fs = require('fs');
//   // Synchron
//   const file = fs.readdirSync('./');
//   console.log('Files: ' + file);

//   // Asynchron
//   fs.readdir('./', function(err, files){ //callback-function or as an Arrow-function
//     if (err) console.log('Error', err);
//     else console.log('Result', files);
//   });

// Working with File-Streams
// const fs = require('fs');

// const readSteam = fs.createReadStream('./docs/blog1.txt',{encoding: 'utf-8'});

// readSteam.on('data', (chunk) =>{
//   console.log('---------NEW CHUNK-------');
//   console.log(chunk);
// });

// -----------------------------------------------------------

// Wokring with events
// const EventEmitter = require('events');   //If the first letter of every word is a capital --> It is a class
// const emitter = new EventEmitter();

// // First register a listener, Then emit the event
// // Register a listener (to listen on the event 'messageLogged')
// emitter.on('messageLogged', (arg) => {  //Arrow-function
//   console.log('Listener called', arg)
// });

// // Raise an event
// emitter.emit('messageLogged', {id: 1, url:'http://'}); // emit = making a noise, produce - signalling

// -----------------------------------------------------------

// Working with own Modules + events
// const Logger = require('./Modules/logger');
// const logger = new Logger();

// logger.on('messageLogged', (arg) => {  //Arrow-function
//   console.log('Listener called', arg);
// });

// logger.log('message');

// -----------------------------------------------------------


// Creating a HTTP - Server
// const http = require('http');

// const server = http.createServer((req, res) => {
// console.log(req.url, req.method);
//   if (req.url === '/'){
//     res.setHeader('Conten-Type', 'text/html');
//     res.write('<p>Hello</p>');
//     res.end();
//   }

//   if(req.url === '/api/courses'){
//     res.write(JSON.stringify([1, 2, 3]));
//     res.end();
//   }
// }); //server has inside a Event-Emitter

// server.listen(3000);

// console.log('Listening on port 3000...')

//---- 

// Sending a HTMl -Page to the Browser
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
console.log(req.url, req.method);
  if (req.url === '/'){
    res.setHeader('Conten-Type', 'text/html');
    fs.readFile('./views/index.html', (err, data) => {
      if (err){
        console.log(err);
        res.end();
      } else {
        res.end(data);
      }
    });
  } else {
    res.end();
  }
});

server.listen(3000, () =>{
  console.log('Listening on port 3000...');
});