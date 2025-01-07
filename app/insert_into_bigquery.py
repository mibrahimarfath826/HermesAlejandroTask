from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
import logging

def insert_into_bigquery(dataset, table, data):
    """
    Inserts data into a BigQuery table with robust error handling.

    Args:
        dataset (str): The BigQuery dataset name.
        table (str): The BigQuery table name.
        data (list): The data to insert, a list of dictionaries.

    Returns:
        None
    """
    client = bigquery.Client()

    # Construct the full table ID
    table_id = f"{client.project}.{dataset}.{table}"

    try:
        # Prepare rows for insertion
        rows_to_insert = []
        
        # Extract and format rows for Python blogs
        for item in data:
            if "title" in item and "link" in item:
                rows_to_insert.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "source": "python_blogs"
                })
            elif "name" in item and "url" in item:  # Extract and format rows for GitHub repos
                rows_to_insert.append({
                    "name": item.get("name", ""),
                    "url": item.get("url", ""),
                    "source": "github_repos"
                })

        # Check if there is data to insert
        if not rows_to_insert:
            logging.warning("No valid data to insert into BigQuery.")
            return

        # Insert rows into BigQuery
        try:
            errors = client.insert_rows_json(table_id, rows_to_insert)
            if errors:
                logging.error(f"Errors occurred while inserting rows: {errors}")
            else:
                logging.info(f"Data successfully inserted into {table_id}.")
        except GoogleAPIError as e:
            logging.error(f"Google API Error during data insertion: {e.message}")
        except Exception as e:
            logging.error(f"Unexpected error during data insertion: {e}")

    except GoogleAPIError as e:
        logging.error(f"Google API Error while preparing data: {e.message}")
    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
