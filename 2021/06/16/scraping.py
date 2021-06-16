from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://www.simplex.inc'
# url = 'https://note.com/sumiiyaaax/'
response = req.urlopen(url)
print(response)
parse_html = BeautifulSoup(response, 'html.parser')
title_lists = parse_html.find_all('a')
title_list = []
url_list = []

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])

title_list
url_list