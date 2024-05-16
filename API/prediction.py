from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import json

model = load_model('Models/model.h5')
new_data = pd.read_csv('./Datasets/Updated_sentiment.csv')

def make_predictions(new_data, model, time_step=30):
    scaler = MinMaxScaler(feature_range=(0, 1))
    new_cp_data = new_data['cp'].values.reshape(-1, 1)
    new_sentiment_data = new_data['Sentiment_Score'].values.reshape(-1, 1)
    scaled_new_cp_data = scaler.fit_transform(new_cp_data)
    new_df = np.concatenate([scaled_new_cp_data, new_sentiment_data], axis=1)
    
    new_X = []
    for i in range(len(new_df) - time_step):
        a = new_df[i:(i+time_step), :]
        new_X.append(a)
    new_X = np.array(new_X)

    predictions = model.predict(new_X)
    scaled_predictions = scaler.inverse_transform(predictions)

    y_true = new_cp_data[time_step:]
    y_pred = scaled_predictions

    # Print the last predicted price
    last_predicted_price = y_pred[-1][0]
    return last_predicted_price

last_predicted_price = make_predictions(new_data, model)
print(last_predicted_price)

# Convert float32 to Python float
last_predicted_price = float(last_predicted_price)

with open('predicted_price.json', 'r') as json_file:
    predicted_price_dict = json.load(json_file)

# Save predicted price as JSON
predicted_price_dict['last_predicted_price'] =  last_predicted_price
with open('predicted_price.json', 'w') as json_file:
    json.dump(predicted_price_dict, json_file)

print("Predicted price saved successfully as 'predicted_price.json'")