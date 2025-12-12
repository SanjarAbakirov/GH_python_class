const PORT = 8000
const axios = require('axios')
const cheerio = require('cheerio')
const express = require('express')

const app = express()

const url = 'https://www.theguardian.com/uk'

axios(url)
    .then(response => {
        const html = response.data
        const $ = cheerio.load(html)
        $('.<title>Democrats release more photos from Jeffrey Epstein estate as congressman says new batch ‘raises even more questions’ – live | US politics | The Guardian</title>', html).each(function () {
            $(this).text()
            $(this).attr('href')
        }

        )
    })

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))