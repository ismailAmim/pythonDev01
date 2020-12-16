import part03
# oriented objects programming
# objects
# refrences
# x= 1000
# python create a variable refernece int
# and the value is 1000
# x= 500
# int are immutable onjects
# python create another int object for 500
# then point the x reference to 500
# x= y
# python will point the y refernce to 500 object
# take a look and test with id() function
a = 25
print(id(a))
b = 58
print(id(b))
b = a
print(id(b))
# testing ref
# testing ids
print(id(a) == id(b))
# testing by is function
print(a is b)
print(a is None)
t = 5
print(id(t))
# t+=2
# t refere to 5 int
# create an int for 2
# create an int for 5+2= 7
# then point to 7 object
t += 2
print(id(t))
# python makes changes by ref
r = [2, 4, 6]
print(r)
s = r
print(r)
# if we make changes in s
# the same changes happens to r
# because s and r refere  to the same

s[2] = 30
print(s)
print(r)
print(id(s))
print(id(r))
print(s is r)

# variables ar named refrences - point to an object
p = [4, 7, 11]
q = [4, 7, 11]
# p and q have the same value
print(p == q)
# p and q referes to different objects
print(p is q)
print(id(p))
print(id(q))
# ids of p and q are different
# values comparison can be controlled programatically
# ids are only affected by the python

# 2 arguments passing
m = [9, 15, 24]

# we pass a ref argument to th function


def modify(k):
    k.append(39)
    print("k =", k)
    print(m is k)


# m  and k  argument referes to the same object
modify(m)

f = [14, 23, 37]


def replace(g):
    g = [17, 28, 45]
    print("g =", g)
# first the g ref refre to  [14,23,37]
# then we change the g ref to a new list [17,28,45]
# so f and g refre to differnt lists


replace(f)
# f still refere to [14,23,37] outside the function
print(f)
# if you want to change the content use this method


def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g =", g)


replace_contents(f)
print("f =", f)


def func(d):
    return d


c = [6, 10, 16]
# we assign the ref not the value,
# no double object allocation in memory
e = func(c)
print(c is e)
# pass by object references
# the value of the reference is copied ,
# not the value of the object

# 2 function argument in details
# def function(a , b = value )
# default value for b


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


# banner shows the message and the deafault border
banner("this is the right time")
# we can change the second argument by passing another value
banner("this is the right time", "*")
# we can soft documenting by using the key arguments
# we should use the key arguments after the position args
banner("this is the right time", border="*")
# you have to supply them in any order
banner(border="*", message="this is the right time")
# the default argument values are evaluated only once
# when def statement is evaluated
# its confusing when using mutable collections


def add_spam(menu=[]):
    menu.append("spam")
    print(menu)
    return menu


breakfast = ["bacon", "eggs"]
add_spam(breakfast)
lunch = ['backed beans']
add_spam(lunch)
# if we are uing mutable vars
add_spam()
add_spam()
# the empty list is created in the first call
# then its still used for the next calls not a new one created
# the solution for is to pass the None value to the arg


def add_spam2(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    print(menu)
    return menu


add_spam2()
add_spam2()
add_spam2(lunch)
add_spam2(lunch)

# 4  Typing
# python is a dynamic and strong typing system
# dynamic object types are only resolved at runtime


def add(a, b):
    return a + b


# change dynamically the args types
print(add(1, 2))
print(add(3.1, 2.4))
print(add("news", "paper"))
print(add([1, 2], [3, 4]))

# strong type system there is no implicit type conversion
# can't run , can't convert  int to string
# we should put only the same types args
# print(add("past ", 23)) / error type mis  match

# variables scoping
# object references have no type
# types of scopes
# 1 local scope context, word
# 2 enclosing sys, urlopen , fetch_words
# 3 global , global count
# 4 built-in , __name__

# everything is an object
print(type(part03))
print(dir(part03))
print(type(part03.square))
print(dir(part03.square))
print(part03.square.__dict__)

# you can multiply a string by an integer
#   produces a new string with multiple copies of the operand
#   this is called the repitiion operation
