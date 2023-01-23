from bs4 import BeautifulSoup
import requests

url = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

discovery_tiles = soup.find("div", {"class": "discovery-tiles"})

spans = discovery_tiles.find_all("span", {"class": "p--small"})

text_attributes = []

for span in spans:
    text_attributes.append(span.text)

for i in range(len(text_attributes)):
    print(str(i + 1) + ": " + text_attributes[i])