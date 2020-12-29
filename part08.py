# variables vs literals

# print(cake)
# NameError: name 'cake' is not defined

import unicodedata
cake = "good"
print(cake)
# "good"

# print("cake "="yummy")
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

# len

# print(len(4))
# TypeError: object of type 'int' has no len()
print(len("something"))
# 9
print(len([1, 45, 78, 9]))
# 4
print(len(""))
# 0
print(len([]))
# 0
unicodedata.lookup("snake")
print(len("🐍"))
# 1
print("🐍")
# "🐍"

# indexing
print("fish"[2])
print("fish"[-2])
# s
print("fish"[-1])
# h
countdown = [3, 2, 1, "blastoff!"]
print(countdown[3])


def start_k(s):
    return s[0] == 'K'


print(start_k("Kelly"))
# True
print(start_k("Abe"))
# False

# indexError

# print("hello!"))
# SyntaxError: unmatched ')'

# print(1+'1')
# type error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print("apple"[5])
# IndexError: string index out of range

# no_words = ""
# print(no_words[0])
# IndexError: string index out of range

# slicing
print("apple"[0])
# a
print("apple"[0:3])
# app
print("apple"[:3])
# app
print("apple"[1:3])
# pp
print("apple"[3:])
# le
print("balloon"[3:8])
# loon
