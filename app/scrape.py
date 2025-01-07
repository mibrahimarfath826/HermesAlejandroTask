import requests
from bs4 import BeautifulSoup

def scrape_python_blogs():
    """
    Scrapes the latest blog posts from the Python.org blogs page.

    This function sends a GET request to the Python.org blogs page, 
    parses the HTML content using BeautifulSoup, and extracts the 
    titles and links of the latest blog posts. The function limits 
    the result to the first 5 blog posts.

    Returns:
        list: A list of dictionaries containing the blog title and link.
              Example:
              [
                  {"title": "Blog Post 1", "link": "https://www.python.org/blogs/post1"},
                  {"title": "Blog Post 2", "link": "https://www.python.org/blogs/post2"}
              ]
    """
    url = "https://www.python.org/blogs/"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # empty list to store blog details
    blogs = []
    
    # Select the first 5 blog posts and extract their title and link
    for item in soup.select('.list-recent-posts li')[:5]:
        title = item.find('a').text  # Extract the blog title
        link = item.find('a')['href']  # Extract the blog link
        blogs.append({"title": title, "link": link})  # Append to the list
    
    # Return the list of blog posts
    return blogs
