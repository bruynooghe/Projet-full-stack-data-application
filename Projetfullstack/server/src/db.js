let mongoose = require('mongoose');
require('dotenv').config()
mongoose.connect(process.env.URL_MONGO+'webAnnonces', { useNewUrlParser: true });
let db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error"));
db.once("open", function(callback){
    console.log("Connection Succeeded");
});

module.exports = db;
