import json
import pandas as pd

# Load log returns from CSV
log_returns = pd.read_csv('./Datasets/log_returns.csv', index_col='Date')

# Parameters
epoch_size = 20
shift = 10

# Compute correlation matrices
correlation_matrices = []
for i in range(0, len(log_returns) - epoch_size, shift):
    subset = log_returns.iloc[i:i + epoch_size]
    correlation_matrix = subset.corr().values.tolist()  # Convert DataFrame to list for JSON serialization
    correlation_matrices.append(correlation_matrix)

# Load and update data from JSON file
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
data_dict = {'correlation': correlation_matrices}

# Write the dictionary to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file)