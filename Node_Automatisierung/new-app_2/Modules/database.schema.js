const mongoose = require("mongoose");

const DATABASE = "mongodb://mymongo:27017/testdb";


mongoose.connect(DATABASE, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true
})
    .then( () => {
        console.log("DB Connected");
    })
    .catch(() => {
        console.log("ERROR in connection!");
    });

const measuringData = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    measuringDate: {
        type: Date,
        required: true,
        default: Date.now
    }
});

module.exports = mongoose.model('Measuring', measuringData);