let mongoose = require("mongoose");
let Schema = mongoose.Schema;
let crypto = require('crypto');

let  UserSchema= new Schema({
    name : String,
    email : String,
    hash : String,
    salt : String
});

UserSchema.methods.setPassword = function(password) {
    this.salt = crypto.randomBytes(16).toString('hex');
    this.hash = crypto.pbkdf2Sync(password, this.salt,
        1000, 64, `sha512`).toString(`hex`);
};

UserSchema.methods.validPassword = function(password) {
    let hash = crypto.pbkdf2Sync(password,
        this.salt, 1000, 64, `sha512`).toString(`hex`);
    return this.hash === hash;
};

let User = mongoose.model("User", UserSchema);
module.exports = User;
