import pandas as pd

def csv_to_json(csv_file, json_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert DataFrame to JSON format
    json_data = df.to_json(orient='records')
    
    # Write JSON data to a file
    with open(json_file, 'w') as f:
        f.write(json_data)

if __name__ == "__main__":
    csv_file = "./Nifty50_data.csv"
    json_file = "Nifty50_data.json"
    
    csv_to_json(csv_file, json_file)
