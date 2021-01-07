const EventEmitter = require('events'); 

class Logger extends EventEmitter { //with extends EventEmitter, the  Logger-Class has all the functionality wich is defined in EventEmitter
  log(message){  //when a function is inside a class, it is a method => no function-Tag is needed
    console.log(message);
      
    // Raise an event
    this.emit('messageLogged', {id: 1, url:'http://'}); //'this.' instead of a new const = emitter .... 'emiter.'
  }
}


module.exports = Logger;