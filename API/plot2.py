from flask import Flask, jsonify, send_file
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
from flask_cors import CORS  

app = Flask(__name__)

# Define a route for generating the heatmap
@app.route('/generate_heatmap')
def generate_heatmap():
    # Load data from JSON files
    with open('data1.json', 'r') as f:
        data1 = json.load(f)

    with open('predicted_price.json', 'r') as f:
        predicted_price = json.load(f)

    # Assuming 'similarities' and 'num_matrices' are keys in the loaded JSON data
    similarities = data1['similarities']
    num_matrices = predicted_price['num_matrices']

    # Generate years range
    years = range(2008, 2025)

    # Generate ticks for x and y axes
    ticks = np.linspace(0, num_matrices - 1, len(years))

    # Plotting
    plt.figure(figsize=(10, 8))

    # Plot heatmap
    heatmap = sns.heatmap(similarities, cmap='viridis', annot=False)

    plt.xticks(ticks, years, color='white')  # Set tick labels color to white
    plt.yticks(ticks, years, color='white')  # Set tick labels color to white

    plt.xlabel('Year', color='white')  # Set x-axis label color to white
    plt.ylabel('Year', color='white')  # Set y-axis label color to white
    plt.title('Similarity Between Consecutive Correlation Matrices', color='white')  # Set title color to white

    # Set color bar text color to white
    cbar = heatmap.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color='white')
    cbar.ax.yaxis.label.set_color('white')

    plt.tight_layout()

    # Save the plot as a temporary file
    plt_path = 'temp_heatmap.png'
    plt.savefig(plt_path, transparent=True)

    # Close the plot
    plt.close()

    # Return the path to the generated plot
    return plt_path

# Define a route for accessing the generated heatmap image
@app.route('/get_heatmap_image')
def get_heatmap_image():
    return send_file('temp_heatmap.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
