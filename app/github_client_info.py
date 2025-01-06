
import requests
def fetch_github_repos(org="google"):
    url = f"https://api.github.com/orgs/{org}/repos"
    response = requests.get(url)
    repos = response.json()[:5]
    return [{"name": repo["name"], "url": repo["html_url"]} for repo in repos]
