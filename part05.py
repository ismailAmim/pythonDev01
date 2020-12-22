from pprint import pprint as pp
import math
# tuples
# delimited by parantheses
# items separated by comma
# contains any type of object
# element access with t[index]
t = ("norway", 4.93, 3)
print(type(t))
print(t[1])
print(len(t))
# adding elements
print(t+(22,))
# duplicating
print(t*3)
# nested tuples
a = ((220, 400), (300, 100))
# access by index
print(a[1][0])
# empty tuple
e = ()
print(type(e))
# other definition without parantheses
tup = 1, 8, 9, 6, 3
print(type(tup))


def minmax(items):
    return min(items), max(items)


# decompose tuple elements
min, max = minmax([5, 8, 7, 3, 9])
print(min, max)
# affecting values
(a, (b, (c, d))) = (4, (8, (9, 7)))
print(a, b, c, d)
# swapping values using tuple swap
print("a, b : before", a, b)
a, b = b, a
print("a, b : after ", a, b)
# create tuple from other iterable
print(tuple([1, 2, 5, 8, 9]))
print(tuple("caramichael"))
# membershipusing in or not in
print(5 in (4, 8, 5, 9))
# strings
# homogenous immutable sequences of unicode codepoints
print(len("amimourismail"))
# concat using + or +=
# use separingly - concat can cause perf degradation" "
s = "new "
s += "york"
print(s)
# create str using join and separator
# "seprartor " or "" whitespace .join[el1,el2,....]
colors = ";".join(["red", "blue", "geen"])
print(colors)
# separate str uing split into table
colors = colors.split(";")
print(colors)
# partition ,divides a str
# into prefix, separator, suffix
# string.partition(separator)
departure, separator, arrival = "london:edingbugh".partition(":")
print(departure, separator, arrival)
# or using underscore for separator
origin, _, destination = "seattle-boston".partition('-')
print(origin, destination)
# format to insert values
print(" the age of {0} is {1}".format("ismail", 32))
print(" the age of {} is {}".format("ismail", 32))
print(" the age of {name} is {age}".format(name="ismail", age=32))
# access values through keys or indexes
pos = (45, 78, 11)
print(
    "the relative posistion is x= {pos[0]} y= {pos[1]} z= {pos[2]}".format(
        pos=pos))


print("Math contants: pi ={m.pi} , e ={m.e}".format(m=math))

# ranges of integers
# range(stop) from 0 to 4
print(range(5))
for i in range(5):
    print(i)
# range(start, stop)
print(list(range(5, 10)))
# range(start, stop, step)
print(list(range(0, 15, 2)))
# python prefer direct iteration
s = [1, 7, 89, 2]
for v in s:
    print(v)
# not using range enumerate
# enumerate for counters
# its yields (index, values) tuples
for v in enumerate(s):
    print(v)
# combined with tuples
for i, v in enumerate(s):
    print("i= {} , v = {} ".format(i, v))

# list
# heterogeneous mutable sequence
# create a splitted list
s = 'show hox to index into sequences'.split()
print(s)
# ['show', 'hox', 'to', 'index', 'into', 'sequences']
# negative indexing from the end to the last
print(s[-2])
# slice [start:stop]
print(s[1:4])
# ['hox', 'to', 'index']
# slicing woks with negative index
print(s[1:-1])
# ['hox', 'to', 'index', 'into']
# slicing fom beginning = [:stop]
print(s[:3])
# ['show', 'hox', 'to']
# slicing from the 3 th to the last one
print(s[3:])
# s[:3] + s[3:] == s
# full slicing
print(s[:])
# slicing is not the same list
print(s is s[:])
# copies are shallow
a = [[1, 2], [3, 4]]
# copie of a  is b its created a different list
# and point to the same sub elements
b = a[:]
print(a is b)
print(a == b)
print(a[0])
print(b[0])
print(a[0] is b[0])
# if we affect to a an other list we use
a[0] = [8, 9]
print(a[0] is b[0])
# a point to new different list
# if we append the same change is occuring
# for the common sub element
a[1].append(5)
print("a [1] =", a[1], "b [1] = ", b[1])
print("list a= ", a)
print("list b= ", b)
# list repitition
# repitition is shallow
# it will create a list of pointers
# that points to the same sub list
lis = [[1, 5]]*5
print(lis)
# if append lis sub list  by one element
# it will be changed in all sub elements
lis[3].append(7)
print(lis)

# list  index (item)
w = "the quick brown fox jumps over the lazy dog".split()
print(w.index('fox'))
# 3
#  print(w.index("unicorn"))
# error !!!
# count occurenses
print(w.count('the'))
# del seq[index] to remove index
# del u[3]
u = "jackdaws love my big sphinx of quartz".split()
del u[3]
print(u)
# remove by value
u.remove("love")
print(u)
# seq.insert(index, item)
u.insert(1, "love")
print(' '.join(u))
# growing lists with + operator
m = [1, 4, 5]
n = [7, 8, 9]
k = m+n
print(k)
# extension with += or .extend()
k += [18, 9, 20]
print(k)
k.extend([45, 78, 99])
print(k)
# reversing and sorting
k.reverse()
print(k)
k.sort()
print(k)
# sorted return a sorted versin of list
y = sorted(k)
print(y)
# reversed return a reversed iterator
y = list(reversed(k))
print(y)
# dict , unordered mapping
# from unique ,immutable keys to mutable keys
urls = {
    "google":      "http://google.com",
    "pluralsight": "http://pluralsight.com",
    "sixty north": "http://sixty-north.com",
    "microsoft":   "http://microsoft.com",
}
print(urls['google'])

# construct a dict from a tuple

names_and_ages = [('alice', 32), ('bob', 48)]
d = dict(names_and_ages)
print(d)
fonetic = dict(a='alpha', b="bee")
print(fonetic)
# dict copying
cp = fonetic.copy()
print(cp)
# or by
cpf = dict(cp)
print(cpf)
# update() update and replace duplicated keys
up = dict(c='cee', g="jai", b="biiiii")
cp.update(up)
print(cp)
# iteration
for key in cp:
    print(" {key} = {value} ".format(key=key, value=cp[key]))
# iterate a series of values

for val in cp.values():
    print(val)

for key in cp.keys():
    print(key)
# items iterations
for key, value in cp.items():
    print(" {key} = {value} ".format(key=key, value=value))
# in and not in work on the keys
# see if the 'a' key is on the dict
print('a' in cp)
# keys immutable
# values mutable
cp['a'] += " ok for you"
print(cp)
cp['q'] = " qyou"
print(cp)
# prety  printing
pp(cp)

# set
# unordered collection of unique , immutable objects
sets = {6, 23, 45, 12, 78}
print(sets)
print(type(sets))
dsets = {}
# empty set, with set()
dests = set()
print(dsets)
# set constructor accept iterables
# duplicates are discarded
s = set([4, 5, 4, 8, 9, 7])
print(s)
print(type(s))
# order is arbitrary
for x in s:
    print(x)
# membership
print(3 in s)
# add elements
s.add(789787)
print(s)
# remove item
s.remove(4)
# copy()
# use set constructor
# copies are shallow
print(s)
scopy = s.copy()
z = set(scopy)
print(z)
# set algebra
blue_eyes = {'olivia', 'harry', 'lily', 'jack', 'amelia'}
blond_hair = {'harry', 'jack', 'amelia', 'mia', 'joshua'}
smell_hcn = {'harry', 'amelia'}
taste_ptc = {'harry', 'lily', 'amelia', 'lola'}
o_blood = {'mia', 'joshua', 'lily', 'olivia'}
b_blood = {'amelia', 'jack'}
a_blood = {'harry'}
ab_blood = {'joshua', 'lola'}
print(blue_eyes.union(blond_hair))
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.difference(blond_hair))
# difference non commutative
print(blue_eyes.difference(blond_hair) == blond_hair.difference(blue_eyes))
# symmetric difference commutative
print(blue_eyes.symmetric_difference(blond_hair))
# issubset non commutative
print(smell_hcn.issubset(blond_hair))
# issuperset
print(taste_ptc.issuperset(smell_hcn))
# disjoint
print(a_blood.isdisjoint(o_blood))
# collections protocols
# container : str, list, range, tuple, bytes, set, dict
# sized     : str, list, renge, tuple, bytes, set, dict
# iterable  : str, list, range, tuple, bytes, set, dict
# sequence  : str, list, range, tuple, bytes
# mutable sequence : list
# mutable set      : set
# mutable mapping  : dict

