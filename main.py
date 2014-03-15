#!/usr/bin/env python
__author__ = 'vasyanya'

import url_model
import city_category_extractor

start_url = "http://job.2gis.ru/vacancy/nsk/"
content = url_model.get_content(url=start_url, use_test_data=True)
cities_data = city_category_extractor.extract(content)

# for city_data in cities_data:
#     print_text = "Link: " + city_data.link
#     if not city_data.category is None:
#         print_text += ", category: " + city_data.category
#     if not city_data.text is None:
#         print_text += ", text: " + city_data.text
#
#     print print_text

named_cities = [cd for cd in cities_data if cd.category is None]
categories = [cd for cd in cities_data if cd.category is not None]

print "Other cities:"
for city in named_cities:
    print "Link: " + city.link + ", text: " + city.text

print "\nCurrent city categories:"
for city in categories:
    print "Category: " + city.category + ", text: " + city.text