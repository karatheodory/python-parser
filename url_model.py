__author__ = 'vasyanya'
import urllib

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
    test_data_file = "test-data.html"
    if use_test_data:
        return load_from_file(test_data_file)

    content = load_url(url)
    if update_test_data:
        save_to_file(content, test_data_file)
    return content