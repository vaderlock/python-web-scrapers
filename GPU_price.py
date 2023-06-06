from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/p/1FT-0015-00010?Item=9SIAG4PJKH4411&Description=GPU&cm_re=GPU-_-9SIAG4PJKH4411-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

title = doc.find("h1", class_="product-title")

prices = doc.find_all(text = "$")
parent = prices[0].parent
strong = parent.find("strong")

print(title.string)
print("$" , strong.string)