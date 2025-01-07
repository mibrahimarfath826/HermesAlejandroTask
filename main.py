from fastapi import FastAPI, status
from app.scrape import scrape_python_blogs
from app.github_client_info import fetch_github_repos
from app.data_handler import combine_data, save_data_to_json
from app.upload_to_bucket import upload_to_gcs
from app.insert_into_bigquery import insert_into_bigquery
import uvicorn

app = FastAPI()

GCS_BUCKET_NAME = "your-gcs-bucket-name"
GCS_FILE_NAME = "combined_data.json"
BIGQUERY_DATASET = "your_dataset"
BIGQUERY_TABLE = "your_table"

@app.get("/data")
async def root():
    # Scrape and Fetch Data
    scraped_data = scrape_python_blogs()
    api_data = fetch_github_repos()
    
    #Combine Data
    combined_data = combine_data(scraped_data, api_data)
    
    # Save Combined Data to Local JSON (optional for debugging)
    save_data_to_json(combined_data)
    
    #Upload Combined Data to GCS
    upload_to_gcs(file_name=GCS_FILE_NAME, data=combined_data, bucket_name=GCS_BUCKET_NAME)
    
    #Insert Combined Data into BigQuery
    insert_into_bigquery(dataset=BIGQUERY_DATASET, table=BIGQUERY_TABLE, data=combined_data)
    
    return {
        "message": "Data processed successfully",
        "data": combined_data,
        "status": status.HTTP_201_CREATED
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)