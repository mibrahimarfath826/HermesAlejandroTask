from fastapi import FastAPI
from app.scrape import scrape_python_blogs
from app.github_client_info import fetch_github_repos
from app.data_handler import combine_data, save_data_to_json

app = FastAPI()

@app.get("/data")
async def root():
    scraped_data = scrape_python_blogs()
    api_data = fetch_github_repos()
    combined_data = combine_data(scraped_data, api_data)
    save_data_to_json(combined_data)
    return combined_data
