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
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/'){
    res.write('Hello');
    res.end();
  }

  if(req.url === '/api/courses'){
    res.write(JSON.stringify([1, 2, 3]));
    res.end();
  }
}); //server has inside a Event-Emitter

server.listen(3000);

console.log('Listening on port 3000...')