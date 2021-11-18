let mongoose = require("mongoose");
let Schema = mongoose.Schema;

let  AnnounceSchema= new Schema({
    name : String,
    country : String,
    owner : String,
    day: String,
    adress : String,
    price: Number
});

let Announce = mongoose.model("Announce", AnnounceSchema);
module.exports = Announce;
