import requests
from bs4 import BeautifulSoup
# pip install beautifulsoup4 lxml

url = 'http://www.supay.com/website/'

response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'lxml')

td = soup.select('td.vip_font')

real_td = td[1]

sanitized = real_td.text.replace('\r', '').replace('\n', '').replace('\t', '')

result = sanitized.split('\xa0')
