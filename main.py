#!/usr/bin/env python
__author__ = 'vasyanya'

import urllib
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


def load_url(url):
    content = urllib.urlopen(url).read()
    return content


def save_to_file(data, file):
    with open(file, "w") as f:
        f.write(data)


def load_from_file(file):
    with open(file, "r") as f:
        return f.read()


content = load_url("http://job.2gis.ru/vacancy/nsk/")

#test_data_file = "test-data.html"
#save_to_file(content, test_data_file)
#content = load_from_file(test_data_file)

soup = BeautifulSoup(content)

links = soup.find_all('a')
for link in links:
    print link.get('href')