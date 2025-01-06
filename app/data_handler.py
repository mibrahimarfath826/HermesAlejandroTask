import json

def save_data_to_json(data, file_path="data_lake/combined_data.json"):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def combine_data(scraped_data, api_data):
    return {"scraped_data": scraped_data, "api_data": api_data}
