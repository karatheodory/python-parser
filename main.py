#!/usr/bin/env python
__author__ = 'vasyanya'

import urllib
from HTMLParser import HTMLParser


def load_url(url):
    content = urllib.urlopen(url).read()
    return content


def save_to_file(data, file):
    with open(file, "w") as f:
        f.write(data)


def load_from_file(file):
    with open(file, "r") as f:
        return f.read()


class TagData:
    def __init__(self):
        self.tag_name = ''
        self.tag_attributes = ''
        self.data = ''


class SortHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.current_tag = None
        self.sorted_tags = {}

    def handle_starttag(self, tag, attributes):
        tag_data = TagData()
        tag_data.tag_name = tag
        #print "Encountered a start tag:", tag
        if len(attributes) != 0:
            #print "Tag attributes:", attributes
            tag_data.tag_attributes = attributes

        self.current_tag = tag_data

        if self.sorted_tags.get(tag_data.tag_name, None) is None:
            self.sorted_tags[tag_data.tag_name] = []
        self.sorted_tags[tag_data.tag_name].append(tag_data)

    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        return

    def handle_data(self, data):
        #print "Encountered some data  :", data
        if self.current_tag is None:
            return
        self.current_tag.data = data

    def get_tag_data_list(self):
        return self.sorted_tags


content = load_url("http://job.2gis.ru/vacancy/nsk/")

#test_data_file = "test-data.html"
#save_to_file(content, test_data_file)
#content = load_from_file(test_data_file)

parser = SortHTMLParser()
parser.feed(content)
sorted_tags = parser.get_tag_data_list()

print "Tag info for links:"
link_data_list = sorted_tags['a']
for tag_data in link_data_list:
    link_attributes = tag_data.tag_attributes
    for attribute in link_attributes:
        attribute_name = attribute[0]
        if attribute_name == 'href':
            attribute_value = attribute[1]
            print "Found link: " + attribute_value