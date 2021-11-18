require('dotenv').config();

const dbMongoose = require('./db');
const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')
const app = express()

const Announce = require('../controllers/announce')
const User = require('../controllers/user')

app.use(morgan('combined'))
app.use(bodyParser.json())
app.use(cors())


app.get('/api/login', User.login)
app.post('/api/signUp', User.signUp)
app.get('/api/getAllAnnounces', Announce.getAllAnnounces)
app.post('/api/postAnnounce', Announce.postAnnounce)

app.listen(process.env.PORT || 8081)