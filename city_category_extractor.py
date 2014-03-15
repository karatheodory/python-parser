__author__ = 'vasyanya'

from bs4 import BeautifulSoup
import re


class CityCategoryData:
    def __init__(self):
        self.link = ''
        self.category = None
        self.text = None


def extract(content):
    soup = BeautifulSoup(content)
    results = []
    all_links = soup.find_all('a')
    vacancy_link_regex_text = '/vacancy/(?P<city>\w+)/(?:category/#(?P<category>\w+))?'
    vacancy_link_regex = re.compile(vacancy_link_regex_text, re.UNICODE)

    for link in all_links:
        href = link.get('href')
        if not 'vacancy' in href:
            continue

        # Parse link
        m = vacancy_link_regex.match(href)
        groups = m.groups()
        city = groups[0]
        category = groups[1]

        # Analyse parsed data. City is required, category and text are optional.
        data = CityCategoryData()
        data.link = city

        print_text = "City: " + city
        if not category is None:
            print_text += ", category: " + category
            data.category = category

        text = link.getText()
        if len(text) > 0:
            print_text += ", text: " + text
            data.text = text
        #print print_text
        results.append(data)
    return results