import sys
import requests
from bs4 import BeautifulSoup as soup
ip = sys.argv[1]
res = requests.get('https://ipinfo.io/'+ip)

res.raise_for_status()
page_soup = soup(res.text,'html.parser')
print(soup.prettify(page_soup))
