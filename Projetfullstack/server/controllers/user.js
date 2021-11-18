const User = require('../models/User')

exports.login = async function (req, res){
    user = await User.findOne({ email : req.query.email })
    if (user === null) {
        return res.status(203).send({
            message : "User not found."
        });
    }
    else {
        if (user.validPassword(req.query.password)) {
            return res.status(201).send({
                name : user.name,
                email: user.email,
                id : user._id
            })
        }
        else {
            return res.status(202).send({
                message : "Wrong Password"
            });
        }
    }
}

exports.signUp = async function(req, res){
    userFind = await User.findOne({ email : req.body.email })
    if (userFind)
        return res.status(205).send({
            message : "Un compte est déjà associé à cette adresse"
        });
    let newUser = new User();
    newUser.name = req.body.name;
    newUser.email = req.body.email;
    newUser.password=req.body.password
    newUser.setPassword(req.body.password);

    // Save newUser object to database
    user = await newUser.save();
    return res.status(201).send({
        id : user._id
    })

}