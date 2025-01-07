import requests

def fetch_github_repos(org="google"):
    """
    Fetches a list of repositories for a given GitHub organization.

    This function sends a GET request to the GitHub API to retrieve the 
    repositories of the specified organization. By default, it fetches 
    repositories for the 'google' organization. The function limits the 
    result to the first 5 repositories.

    Args:
        org (str): The GitHub organization name (default is "google").

    Returns:
        list: A list of dictionaries containing the repository name and URL.
              Example:
              [
                  {"name": "repo1", "url": "https://github.com/google/repo1"},
                  {"name": "repo2", "url": "https://github.com/google/repo2"}
              ]
    """
    # Construct the API URL for the specified organization
    url = f"https://api.github.com/orgs/{org}/repos"
    
    # Send a GET request to the GitHub API
    response = requests.get(url)
    
    # Parse the JSON response and limit to the first 5 repositories
    repos = response.json()[:5]
    
    # Extract and return the repository name and URL
    return [{"name": repo["name"], "url": repo["html_url"]} for repo in repos]
