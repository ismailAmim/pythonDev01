# $$import part03
from urllib.request import urlopen

# module fetch_words definition


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(items):
    for item in items:
        print(item)


def main():
    url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_words(words)

# print(__name__)
