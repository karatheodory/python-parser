#!/usr/bin/env python
__author__ = 'vasyanya'


from bs4 import BeautifulSoup
import re
import url_model

start_url = "http://job.2gis.ru/vacancy/nsk/"
content = url_model.get_content(start_url, True)

soup = BeautifulSoup(content)

all_links = soup.find_all('a')
vacancy_link_regex_text = '/vacancy/(?P<city>\w+)/(?:category/#(?P<category>\w+))?'
vacancy_link_regex = re.compile(vacancy_link_regex_text)

for link in all_links:
    href = link.get('href')
    if not 'vacancy' in href:
        continue
    m = vacancy_link_regex.match(href)
    groups = m.groups()
    city = groups[0]
    category = groups[1]

    text = link.getText()
    print_text = "City: " + city
    if not category is None:
        print_text += ", category: " + category

    if len(text) > 0:
        print_text += ", text: " + text
    print print_text
