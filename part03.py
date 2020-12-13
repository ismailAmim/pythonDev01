#!/usr/bin/env python3
# the whole shebang
# pylauncher
# create an executable py.exe and is on the path
# associated with *.py files
# parse shebangs to locate the correct python interpreter
"""#"!/usr/bin/env python3 """
# works for windows,
# controls module sexecution by the program loader

# modularity import
# import part 02 module
# or from module import sub module
import part02
#from part02 import fetch_words
""" from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word) """
"""print(story_words)
for word in story_words:
    print(word)"""

# defining functions
# and returning values
# input x and return square value


def square(x):
    return x*x


print(square(16))


def launch_missiles():
    print("missiles launched")


launch_missiles()


def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")


even_or_odd(5)
# part02.fetch_words()

# special attributes in python
# are delimited by double underscores
# __name__ ex: __main__
# __name to dtermine how the module is being used
# main functions and command line arguments
if __name__ == '__main__':
    part02. main()
# help function to display all
# infos that you have made in your documentation
# docstrings
help(part02)

""" 
 Documenting your code 
 using docstrings 
 """
