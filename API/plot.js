const express = require('express');
const cors = require('cors');
const fs = require('fs');

const app = express();
const port = 3001;

app.use(cors());

const correlationData = fs.readFileSync('predicted_price.json', 'utf8');
const correlationMatrix = JSON.parse(correlationData).last_correlation_matrix;

const similarityData = fs.readFileSync('data1.json', 'utf8');
const similarityMatrix = JSON.parse(similarityData).similarities;

const tickerSymbolsWithNames = {
    '^NSEI': 'Nifty 50',
    '^BSESN': 'BSE Sensex',
    '^NSEBANK': 'NSE Bank',
    '^HSI': 'Hang Seng',
    '^TWII': 'Taiwan Weighted',
    '^AXJO': 'S&P/ASX 200',
    '^SET.BK': 'SET',
    '^JKSE': 'Jakarta Composite',
    '000001.SS': 'SSE Composite',
    '000300.SS': 'CSI 300',
    '^N225': 'Nikkei 225',
    '^TPX': 'TOPIX',
    '^STI': 'Straits Times',
    '^IXIC': 'NASDAQ Composite',
    '^NYA': 'NYSE Composite',
    '^GSPC': 'S&P 500',
    '^GSPTSE': 'S&P/TSX Composite',
    '^MXX': 'IPC',
    '^MERV': 'MERVAL',
    '^BVSP': 'Bovespa',
    '^IPSA': 'IPSA',
    '^GDAXI': 'DAX',
    '^FCHI': 'CAC 40',
    '^IBEX': 'IBEX 35',
    '^SSMI': 'SMI',
    '^AEX': 'AEX',
    '^BFX': 'BEL 20',
    '^ATX': 'ATX',
    '^PX': 'PX',
    '^BUX': 'BUX',
    '^TA-25': 'TA-25',
    '^KS11': 'KOSPI',
    '^XU100.I': 'BIST 100',
    '^ISEQ': 'ISEQ 20',
};

app.get('/correlation_heatmap', (req, res) => {
    res.json(correlationMatrix);
});

app.get('/similarity_matrix', (req, res) => {
    console.log(similarityMatrix);
    res.json(similarityMatrix);
   
});

app.get('/', (req, res) => {
    res.render('index', { tickerSymbolsWithNames });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
