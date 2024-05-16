import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import MDS
from sklearn.cluster import KMeans
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import json

closing_prices_df = pd.read_csv('./recent.csv', index_col='Date')
stock_data_df = pd.read_csv('./Datasets/stock_data.csv', index_col='Date')

# # Get the sets of column names for each DataFrame
# closing_prices_columns = set(closing_prices_df.columns)
# stock_data_columns = set(stock_data_df.columns)

# # Check if the column sets are the same
# if closing_prices_columns == stock_data_columns:
#     print("Both DataFrames have the same columns.")
# else:
#     print("The columns of the two DataFrames are not the same.")

combined_df = pd.concat([stock_data_df, closing_prices_df], axis=0, sort=False)

with open('data.json', 'r') as f:
    data = json.load(f)

# Extract correlation data
correlation_matrices_json = data['correlation']

# Convert correlation data from dictionary to DataFrame
correlation_matrices = [pd.DataFrame(cm) for cm in correlation_matrices_json]

numeric_combined_df = combined_df.select_dtypes(include='number')

last_subset = numeric_combined_df.iloc[-20:]
last_correlation_matrix = last_subset.corr()

correlation_matrices.append(last_correlation_matrix)

with open('predicted_price.json', 'r') as file:
    data = json.load(file)

data['last_correlation_matrix'] = last_correlation_matrix.to_dict()

# Save the updated data back to the JSON file
with open('predicted_price.json', 'w') as file:
    json.dump(data, file, indent=4)

def calculate_similarity_matrix(matrix1, matrix2):
    absolute_difference = np.abs(matrix1 - matrix2)
    similarity = absolute_difference.mean().mean()
    return similarity

num_matrices = len(correlation_matrices)
epochs_per_year = 25

similarity_matrix = np.zeros((num_matrices, num_matrices))

for i in range(num_matrices):
    for j in range(num_matrices):
        similarity_matrix[i, j] = calculate_similarity_matrix(correlation_matrices[i], correlation_matrices[j])

null_indices = np.isnan(similarity_matrix)

# Replace null values with zeros
similarity_matrix[null_indices] = 0

mds = MDS(n_components=3, dissimilarity='precomputed', random_state=42)
mds_coordinates = mds.fit_transform(similarity_matrix)

# Step 2: Predict the cluster for the last similarity
last_similarity_coordinates = mds_coordinates[-1].reshape(1, -1)  # Reshape for compatibility with clustering
kmeans = KMeans(n_clusters=4)  # Define the number of clusters
kmeans.fit(mds_coordinates[:-1])  # Fit KMeans on all but the last similarity
cluster_labels = kmeans.fit_predict(mds_coordinates)

similarities_list = similarity_matrix.tolist()
mds_result_list = mds_coordinates.tolist()
cluster_labels_list = cluster_labels.tolist()




predicted_cluster = kmeans.predict(last_similarity_coordinates)

print("Predicted Cluster for the Last Similarity:", predicted_cluster[0])

predictions = int(predicted_cluster[0])

last_similarity_coordinates_list = last_similarity_coordinates.tolist()

# Update data dictionary with lists instead of arrays
data = {
    'predictions': predictions,
    'last_similarity_coordinates': last_similarity_coordinates_list,
    'similarities': similarities_list,
    'mds_result': mds_result_list,
    'cluster_labels': cluster_labels_list
}

# Write data to JSON file
with open('data1.json', 'w') as f:
    json.dump(data, f)





