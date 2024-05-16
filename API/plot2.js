const express = require('express');
const cors = require('cors');
const fs = require('fs');

const app = express();
const port = 3001;

app.use(cors());

const correlationData = fs.readFileSync('predicted_price.json', 'utf8');
const correlationMatrix = JSON.parse(correlationData).last_correlation_matrix;

const data = fs.readFileSync('data1.json', 'utf8');
const similarityMatrix = JSON.parse(data).similarities;
const last_coordinates = JSON.parse(data).last_similarity_coordinates
const labels = JSON.parse(data).cluster_labels
const mds = JSON.parse(data).mds_result

const data1 = fs.readFileSync('data.json', 'utf-8');
// const correlationMatrices = JSON.parse(data1).correlation;

app.get('/mds', (req, res) => {
  const responseData = {
    last_coordinates: last_coordinates,
    labels: labels,
    mds: mds
  };
  res.json(responseData);
});

app.get('/correlation_heatmap', (req, res) => {
  res.json(correlationMatrix);
});

app.get('/similarity_matrix', (req, res) => {
  res.json(similarityMatrix);
});

app.get('/correlation_matrices', (req, res) => {
  res.json(correlationMatrices);
});

app.listen(port, () => {
  // No console.log statement here
});