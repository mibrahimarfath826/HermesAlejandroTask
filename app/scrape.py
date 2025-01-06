import requests
from bs4 import BeautifulSoup

def scrape_python_blogs():
    url = "https://www.python.org/blogs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    blogs = []

    for item in soup.select('.list-recent-posts li')[:5]:
        title = item.find('a').text
        link = item.find('a')['href']
        blogs.append({"title": title, "link": link})

    return blogs


