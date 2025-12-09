const PORT = 8000
const axios = require('axios')
const cheerio = require('cheerio')
const express = require('express')

const app = express()

const url = 'https://www.theguardian.com/international'

axios(url)
    .then(response => {
        response.data
    })

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))