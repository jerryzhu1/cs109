import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
import time
import dash
import dash_core_components as dcc
import dash_html_components as html



# data extraction
def html_parsing(line):
    record = []
    title = line.find("a", class_= re.compile('title*')).text
    time_submitted_obj = line.find("time")
    time_sub = time_submitted_obj['datetime']
    author = line.find("a", class_='author').text
    comments = line.find("a", class_= ('bylink'))['href']
    record = [title, time_sub, author, comments]
    return record

# web crawling
url = "https://old.reddit.com/top/"
r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find("div", id = 'siteTable')
block  = table.findAll("div",attrs={'class':re.compile("thing*")})

records = []
for line in block:
    record = html_parsing(line)
    records.append(record)

# data transformation
df = pd.DataFrame(records, columns=['title', 'time_submitted', 'author', 'comments link'])
print(df)
