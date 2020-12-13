# list mutable sequences of objects

from urllib.request import urlopen
from urlib.request import urlopen
l = [1, 2, 3]
print(l[1])
a = ["apple", "orange", "pear"]
print(a[1])
a[1] = 7
print(a[1])
b = []
b.append(1.68)
print(b)
b.append(1.414)
print(b)
# create a list from a string
lc = list("characters")
print(lc)
c = ['bear',
     'giraffe',
     'elephant', ]
print(c)

# dictionaries
# dict mutable mappings of keys to values
# k1: v1 , k2:v2

d = {'alice': '29121988', 'bob': '25521454', 'eve': '23121990'}
print(d)
print(d['alice'])
d['charles'] = '24121991'
print(d)
e = {}
print(e)

# for loops
# for item in iterable :
# ... body ...
cities = ["london", "new york", "paris"]
for city in cities:
    print(city)
colors = {'crismon': 0x123, 'coral': 0xff7f50}
for c in colors:
    print(c, colors[c])
# put all together
