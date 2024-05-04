// app.js
const express = require('express');
const path = require('path');
const app = express();
const axios = require('axios');
const port = 3000;

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://127.0.0.1:3010/price');
        const bitcoinPriceData = response.data;
        // const bitcoinPrice = parseFloat(bitcoinPriceData['bpi']['USD']['rate'].replace(',', ''));
        const bitcoinPrice = bitcoinPriceData.price.toFixed(2);
        console.log(bitcoinPrice);
        
        let data = {
            name: 'Dyuti Dasmahapatra',
            type: 'chomu'
        };
        res.render('home', { data: data, bitcoinPrice: bitcoinPrice });
    } catch (error) {
        console.error('Error fetching Bitcoin price:', error);
        res.status(500).send('Error fetching Bitcoin price');
    }
});
app.get('/index', async (req, res) => {
    const response = await axios.get('http://127.0.0.1:3010/price');
    const bitcoinPriceData = response.data;
    // const bitcoinPrice = parseFloat(bitcoinPriceData['bpi']['USD']['rate'].replace(',', ''));
    const bitcoinPrice = bitcoinPriceData.price.toFixed(2);
    console.log(bitcoinPrice);

    res.render('index',{ bitcoinPrice: bitcoinPrice });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
