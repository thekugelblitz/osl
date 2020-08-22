import requests
from bs4 import BeautifulSoup as soup

res = requests.get('https://ipinfo.io/1.1.1.1')
#res = requests.get('https://host.io/nimlo.in')

res.raise_for_status()
page_soup = soup(res.text,'html.parser')
print(soup.prettify(page_soup))
