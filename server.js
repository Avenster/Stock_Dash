// app.js
const express = require('express');
const path = require('path');
const app = express();
const axios = require('axios');
const port = 3000;
const fs = require('fs');

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'public')));


app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://127.0.0.1:3020/price');
        const bitcoinPriceData = response.data;
        // const bitcoinPrice = parseFloat(bitcoinPriceData['bpi']['USD']['rate'].replace(',', ''));
        const nifty = bitcoinPriceData.home_price[0];
        const bse = bitcoinPriceData.home_price[1];
        const sp = bitcoinPriceData.home_price[2];
        
        
        
        res.render('home', { nifty:nifty,bse:bse,sp:sp });
    } catch (error) {
        console.error('Error fetching Bitcoin price:', error);
        res.status(500).send('Error fetching Bitcoin price');
    }
});
app.get('/index', async (req, res) => {
    const response = await axios.get('http://127.0.0.1:3020/price');
    const bitcoinPriceData = response.data;
    const bitcoinPrice = bitcoinPriceData.prices[0];
    const uniquePrices = bitcoinPriceData.unique_prices;
    const uniquePerct = bitcoinPriceData.unique_perct;
    const stockNames = ["Nifty 50", "Sensex", "Nifty B", "Nifty IT"];


    console.log(bitcoinPrice);
    console.log(uniquePrices);
    console.log(uniquePerct);

    res.render('index', {
        bitcoinPrice: bitcoinPrice,
        uniquePrices: uniquePrices,
        uniquePerct: uniquePerct,
        stockNames:stockNames
    });
});

app.get('/sp500', async (req, res) => {
    const response = await axios.get('http://127.0.0.1:3020/price');
    const bitcoinPriceData = response.data;
    const bitcoinPrice = bitcoinPriceData.prices[1];
    const uniquePrices = bitcoinPriceData.unique_prices;
    const uniquePerct = bitcoinPriceData.unique_perct;
    const stockNames = ["Nifty 50", "Sensex", "Nifty B", "Nifty IT"];


    console.log(bitcoinPrice);
    console.log(uniquePrices);
    console.log(uniquePerct);

    res.render('sp500', {
        bitcoinPrice: bitcoinPrice,
        uniquePrices: uniquePrices,
        uniquePerct: uniquePerct,
        stockNames:stockNames
    });
});

app.get('/correlation', async (req, res) => {
   
    const jsonData = JSON.parse(fs.readFileSync('API/data1.json', 'utf8'));
    const predictedPrice = JSON.parse(fs.readFileSync('API/predicted_price.json'));
    const predictions = jsonData["predictions"];
    const price = predictedPrice["last_predicted_price"];
    const similarityMatrix = jsonData.similarities; // Adjust this according to your actual data structure

    
    res.render('correlation', {
        prediction: predictions,
        lastPredictedPrice: price,
        similarityMatrix: similarityMatrix,
    });
  });

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
