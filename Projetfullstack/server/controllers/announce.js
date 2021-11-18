const Announce = require('../models/Announce')


exports.getAllAnnounces= async function (req, res) {
    let announces = await Announce.find();
    if (announces.length === 0)
    {
        res.status(400).send()
    }
    else{
        console.log(announces)
        res.status(201).send({
            data: announces
        })
    }
};

exports.postAnnounce = async function (req, res) {
    const today = new Date();
    date = today.getDay()+'/'+today.getMonth()+'/'+today.getFullYear()
    let annouce = new Announce();
    annouce.name = req.body.name
    annouce.country = req.body.country
    annouce.owner = req.body.owner
    annouce.adress = req.body.adress
    annouce.price = req.body.price
    annouce.day = date
    await annouce.save()
    let announces = await Announce.find();
    res.status(201).send({data:announces})
};