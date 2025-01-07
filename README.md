# Python Blog and GitHub Data Aggregator

This project aggregates the latest blog posts from Python.org and repositories from a specified GitHub organization. It combines the data into a single JSON object and provides an API endpoint to fetch the combined data. Additionally, the combined data can be saved to a local JSON file.

---

## Features

- Scrapes the latest blogs from [Python.org Blogs](https://www.python.org/blogs/).
- Fetches the latest repositories from a specified GitHub organization using the GitHub API.
- Combines both datasets into a single JSON object.
- Exposes an API endpoint to retrieve the combined data.
- Saves the combined data into a local JSON file for persistence.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Pip (Python package manager)

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:mibrahimarfath826/HermesAlejandroTask.git
cd HermesAlejandroTask
``` 
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:
```

```bash
pip install -r requirements.txt
```

## Dependencies
# The following Python libraries are used in this project:

1. fastapi – For building the web API.
2. requests – For making HTTP requests.
3. beautifulsoup4 – For web scraping.
4. uvicorn – For running the FastAPI application.


## Usage
# Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```
Access the API endpoint:

Open your browser or use a tool like curl or Postman to access:
```bash
http://127.0.0.1:8000/data
```
The response will be a JSON object containing:
Latest blog posts from Python.org.
Latest repositories from the specified GitHub organization.