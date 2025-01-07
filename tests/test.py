def test_scraper():
    from app.scrape import scrape_python_blogs
    assert len(scrape_python_blogs()) > 0

def test_api_client():
    from app.github_client_info import fetch_github_repos
    assert len(fetch_github_repos()) > 0
