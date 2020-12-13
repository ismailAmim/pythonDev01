# $$import part03
from urllib.request import urlopen

# module fetch_words definition
"""
 retreive and print words from a url
 
 Usage : python dev level 01 
 """


def fetch_words(url):
    """  fetch a list of all words from a url repo
        args:
             url to a text document
        return :
             list of strings con """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(items):
    """ print each word seprately
    args: 
        iterable series of items"""
    for item in items:
        print(item)


def main():
    """print each word from a url """
    url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_words(words)

# print(__name__)
