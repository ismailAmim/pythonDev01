# types of comprehensions
# list comprehensions
# set comprehensions
# dict comprehensions
from itertools import islice, count, chain
from pprint import pprint as pp
import math
words = "ok  to persue your dreams by taking realistic objectifs".split()
# list comprehension [ exp(var) for var in iterable]
print([len(word) for word in words])
print([len(str(math.factorial(x))) for x in range(20)])
# [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
# set comprehensions {exp(var) for var in iterable}
print({len(str(math.factorial(x))) for x in range(20)})
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
# dict comprehension {key_exp:value_exp for item in iterable}
country_to_capital = {"united kingdom": "london",
                      "brazil": "brazilia"}
capital_to_country = {capital: country for country,
                      capital in country_to_capital.items()}
pp(capital_to_country)
#  {'brazilia': 'brazil', 'london': 'united kingdom'}
words = ['hi', 'hello', 'foxtrot', 'hotel']
print({x[0]: x for x in words})
# {'h': 'hotel', 'f': 'foxtrot'}
# duplicates keys are replaced
# h : hotel
# don't cram too much complexity into comprehensions
# filtering predicates
# [ exp(var) for var in iterable if predicate(item)]


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


print([x for x in range(101) if is_prime(x)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
# 71, 73, 79, 83, 89, 97]
# prime square divisors
pp({x*x: (1, x, x*x) for x in range(101) if is_prime(x)})
"""
{4: (1, 2, 4),
 9: (1, 3, 9),
 25: (1, 5, 25),
 49: (1, 7, 49),
 121: (1, 11, 121),
 169: (1, 13, 169),
 289: (1, 17, 289),
 361: (1, 19, 361),
 529: (1, 23, 529),
 841: (1, 29, 841),
 961: (1, 31, 961),
 1369: (1, 37, 1369),
 1681: (1, 41, 1681),
 1849: (1, 43, 1849),
 2209: (1, 47, 2209),
 2809: (1, 53, 2809),
 3481: (1, 59, 3481),
 3721: (1, 61, 3721),
 4489: (1, 67, 4489),
 5041: (1, 71, 5041),
 5329: (1, 73, 5329),
 6241: (1, 79, 6241),
 6889: (1, 83, 6889),
 7921: (1, 89, 7921),
 9409: (1, 97, 9409)}
 """
# simple is better than complex
# iteration protocols
# iterable protocol
# iterator = iter(iterable)
# iterator protocol
# item = next(iterator)
iterable = ["spring", "summer", "automn", "winter"]
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# stop iteration the out of index
# print(next(iterator))


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty ")


print(first(["1st", "2nd", "3rd"]))
# 1st
print(first({"1st", "2nd", "3rd"}))
# 1st
# print(first(set()))
# ValueError: iterable is empty
# generators in python
# all genrators are iterators
# the next value is computed on demand
# can model infinite sequences
# are composable into pipelines


def gen123():
    yield 1
    yield 2
    yield 3


gen = gen123()
print(gen)
# <generator object gen123 at 0x0000001E1A7BA120>
print(next(gen))
# 1
print(next(gen))
# 2
print(next(gen))
# 3
# print(next(gen))
# StopIteration
for v in gen123():
    print(v)
"""
1
2
3
"""
h = gen123()
i = gen123()
print(h is i)
# False
print(next(h))
# 1
print(next(h))
# 2
print(next(i))
# 1


def gen246():
    print("yield 2")
    yield 2
    print("yield 4")
    yield 4
    print("yield 6")
    yield 6
    print("about retun")


g = gen246()
print(next(g))
# yield 2
# 2
print(next(g))
# yield 4
# 4
print(next(g))
# yield 6
# 6

# print(next(g))
# about retun
# StopIteration !!!

# stateful generators
# generators resume execution
# can maintain state in local variables
# complex control flow
# lazy evaluation


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


run_take()
"""
2
4
6
"""


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            # it wheel continue even the item is in it
            # but it doesn't yeild  it
            print("continue ", item)
            continue
        yield item
        print("yield ", item)
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print("dis ", item)


print("distinct function")
run_distinct()
"""
distinct function
dis  5
yield  5
dis  7
yield  7
continue  7
dis  6
yield  6
continue  5
continue  5
"""


def run_pipeline():
    items = [3, 6, 6, 3, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


print("run pipeline function")
run_pipeline()
"""
it will pipe distinct function first
then run take second
run pipeline function
3
yield  3
6
yield  6
continue  6
continue  3
1
yield  1
continue  1
"""
# generators comprehensions
# (exp(item) for item in iterable)
million_squares = (x*x for x in range(1, 1000001))
print(million_squares)
# <generator object <genexpr> at 0x000000966C984820>

# exp generator sum
print(sum(x*x for x in range(1, 1000001)))
# 333333833333500000
# islice iterator
twenty_primes = islice((x for x in count() if is_prime(x)), 20)
print(twenty_primes)
# <itertools.islice object at 0x000000573601BA40>
print(list(twenty_primes))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
# 71]
print(any([False, False, True]))
# True
print(all([False, False, True]))
# False
print(any(is_prime(x) for x in range(1328, 1361)))
# False
print(all(name == name.title() for name in ['London', 'New York', 'Sydney']))
# True

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
for item in zip(sunday, monday):
    print(item)
"""
(12, 13)
(14, 14)
(15, 14)
(15, 14)
(17, 16)
(21, 20)
(22, 21)
(22, 22)
(23, 22)
(22, 21)
(20, 19)
(18, 17)
"""
for sun, mon in zip(sunday, monday):
    print("average : ", (sun+mon)/2)
"""
average :  12.5
average :  14.0
average :  14.5
average :  14.5
average :  16.5
average :  20.5
average :  21.5
average :  22.0
average :  22.5
average :  21.5
average :  19.5
average :  17.5
"""
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
for temps in zip(sunday, monday, tuesday):
    print("min = {:4.1f}, average = {:4.1f}, max=  {:4.1f}".format(
        min(temps), max(temps), sum(temps)/len(temps)))
"""
min =  2.0, average = 13.0, max=   9.0
min =  2.0, average = 14.0, max=  10.0
min =  3.0, average = 15.0, max=  10.7
min =  7.0, average = 15.0, max=  12.0
min =  9.0, average = 17.0, max=  14.0
min = 10.0, average = 21.0, max=  17.0
min = 11.0, average = 22.0, max=  18.0
min = 12.0, average = 22.0, max=  18.7
min = 10.0, average = 23.0, max=  18.3
min =  9.0, average = 22.0, max=  17.3
min =  8.0, average = 20.0, max=  15.7
min =  8.0, average = 18.0, max=  14.3
"""
temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))
"""
# True
# iteration tools
sum()
any()
zip()
all()
min()
max()
enumerate()
# standard library itertools
chain()
islice()
count()
many more !
