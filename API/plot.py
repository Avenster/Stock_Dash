import matplotlib
matplotlib.use('Agg')  # Use non-interactive Agg backend

import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, send_file, jsonify
import io
import numpy as np

app = Flask(__name__)

# Parse the JSON data
log_returns = pd.read_csv('Datasets/log_returns.csv', index_col='Date')
with open('predicted_price.json', 'r') as file:
    data = json.load(file)

correlation_matrix_json = data['last_correlation_matrix']

# Convert the correlation data from dictionary to DataFrame
correlation_matrix_df = pd.DataFrame(correlation_matrix_json)
correlation_matrix = correlation_matrix_df.values

ticker_symbols_with_names = {
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
}


@app.route('/correlation_heatmap', methods=['GET'])
def correlation_heatmap():
    plt.figure(figsize=(12, 10), facecolor='none')  # Make the background transparent
    ax = plt.gca()
    im = ax.imshow(correlation_matrix, cmap="viridis")

    # Create a colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.yaxis.set_tick_params(color='white')  # Set the colorbar tick labels to white
    cbar.outline.set_edgecolor('white')  # Set the colorbar outline to white
    cbar.ax.yaxis.label.set_color('white')  # Set the colorbar label to white

    plt.xlabel("Ticker", color='white')  # Set the text color to white
    plt.ylabel("Ticker", color='white')
    ticker_symbols = [ticker.split()[0] for ticker in log_returns.columns]
    plt.xticks(ticks=np.arange(len(log_returns.columns)), labels=[ticker_symbols_with_names[ticker] for ticker in ticker_symbols], rotation=90, color='white')  # Set the tick labels color to white
    plt.yticks(ticks=np.arange(len(log_returns.columns)), labels=[ticker_symbols_with_names[ticker] for ticker in ticker_symbols], rotation=0, color='white')
    ax.set_facecolor('none')  # Make the axis background transparent
    cbar.ax.patch.set_facecolor('none')  # Make the colorbar background transparent

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', transparent=True, bbox_inches='tight', pad_inches=0)  # Save with transparent background
    img_buffer.seek(0)
    plt.clf()
    plt.close()
    return send_file(img_buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
