import json

def save_data_to_json(data, file_path="data_lake/combined_data.json"):
    """
    Saves the provided data to a JSON file.

    This function takes the input data and writes it to a JSON file at the specified 
    file path. If no file path is provided, it defaults to saving the data in 
    'data_lake/combined_data.json'.

    Args:
        data (dict or list): The data to be saved in the JSON file.
        file_path (str): The path where the JSON file will be saved. Default is 
                         'data_lake/combined_data.json'.
    """
    # Open the specified file in write mode
    with open(file_path, 'w') as f:
        # Write the data to the file in JSON format with an indentation of 4 spaces
        json.dump(data, f, indent=4)

def combine_data(scraped_data, api_data):
    """
    Combines the scraped data and API data into a single dictionary.

    This function takes two datasets (scraped data and API data) and combines them 
    into a single dictionary, with separate keys for each dataset.

    Args:
        scraped_data (list): The list of data scraped from a website (e.g., blog titles).
        api_data (list): The list of data fetched from a public API (e.g., GitHub repos).

    Returns:
        dict: A dictionary containing both the scraped and API data under separate keys.
              Example:
              {
                  "scraped_data": [{"title": "Blog 1", "link": "url1"}, ...],
                  "api_data": [{"name": "Repo 1", "url": "url1"}, ...]
              }
    """
    # Combine the scraped and API data into a dictionary
    return {"scraped_data": scraped_data, "api_data": api_data}
