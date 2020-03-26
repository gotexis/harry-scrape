#  https://selenium-python.readthedocs.io/getting-started.html
from pprint import pprint
from selenium import webdriver
import csv

browser = webdriver.Chrome(executable_path="./driver/chromedriver.exe")

b = browser

url = 'https://www.gtrading.com.au/live-rate'

b.get(url)

tbody = b.find_element_by_tag_name('tbody')

rows = tbody.find_elements_by_tag_name('tr')

result = []

for row in rows:
    row_text = row.text.split('\n')
    from_currency = row_text[0]
    to_currency = row_text[1]
    rates = row_text[2].split(' ')

    rate_buy = rates[2]
    rate_sell = rates[3]

    result.append({
        "from_currency": from_currency,
        "to_currency": to_currency,
        "rate_buy": rates[2],
        "rate_sell": rates[3],
    })

# write to CSV
with open('gtrading.csv', 'w') as f:
    output = csv.writer(f)  # create a csv.write
    for row in result:
        output.writerow(row.values())  # values row
