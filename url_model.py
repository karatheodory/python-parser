__author__ = 'vasyanya'
import urllib
import os.path

#<editor-fold description="Helper functions">

def load_url(url):
    content = urllib.urlopen(url).read()
    return content


def save_to_file(data, file):
    with open(file, "w") as f:
        f.write(data)


def load_from_file(file):
    with open(file, "r") as f:
        return f.read()

#</editor-fold>


def get_content(url, use_test_data=False, update_test_data=False):
    test_data_file = url.replace('http://', '').replace('/', '_').replace('?', '').replace('=', '') + ".html"
    if use_test_data and not update_test_data and os.path.isfile(test_data_file):
        return load_from_file(test_data_file)

    content = load_url(url)
    if update_test_data or not os.path.isfile(test_data_file):
        save_to_file(content, test_data_file)
    return content