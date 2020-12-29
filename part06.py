# handling exceptyions
# raise an execption to interrupt program flow
# handle an exception to resume control
# unhandled exceptions will termintate the program
# exceptions objects contain information about the exceptional event
"""def convert(s):
    x = int(s)
    return x


print(convert("3"))
print(convert("bob"))"""
# error invalid entry for bob
# handling errors

# using try except

# convert("string") value error
# convert([4,5,7,6]) type error


import os
from math import log
import sys


def convert_w_h(s):
    ''' testing '''
    try:
        x = int(s)
        print(" conversion succeeded !")
    except (ValueError, TypeError):
        x = -1
        print(" conversion failed ???!")
    return x


"""
print(convert_w_h("15"))
print(convert_w_h("bob"))
print(convert_w_h([14, 12, 13]))
"""

# exceptions for programmer errors
# indentationError
# SyntaxError
# NameError

# import sys


def convert_w_h_2(s):
    ''' testing '''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("converion error :  {}".format(str(e)), file=sys.stderr)
        return -1


#print(convert_w_h_2({14, 545, 23}))

# imprudent errors
# exeptions  cn not be ignored
# but error codes can


def string_log(s):
    v = convert_w_h_2(s)
    return log(v)
# re-raising exceptions

# print(string_log("ouch"))


def convert_raising_err(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error: {}".format(str(e)), file=sys.stderr)
        raise


# print(convert_raising_err("paul"))

# exceptions are part of the api
# callersnedd to know what exceptions to except and when
# use exceptions that users will anticipate
# standard exceptions are often the best choice

def sqrt_c(x):
    if x < 0:
        # raise an exception
        raise ValueError(
            "cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess)/2.0
        i += 1
    return guess


def res():
    try:
        print(sqrt_c(9))
        print(sqrt_c(-40))
    except ValueError as e:
        # print the sqrt_c raised exception
        print(e, file=sys.stderr)

    print("program execution continues normally here")


res()

# exceptions are part of the api
# using common or exiting exceptions types as possible
# IndexError
# KeyError, indexError is out of range
# ValueError, right type but inappropriate value
# TypeError, look-up in mapping fails (like dict)
# etc...

# avoid protecting against typeErrors
# it's  usually not worth checking types
# this can limit your functions unnecessarily

# two philosophies
# look before you leap
# it's easier to ask forgiveness than permission
# local vs non-local handling
# error codes require interspersed; local handling
# exceptions allow centralized non-local handling
# exceptions require explicit handling
# error codes are silent by default

# resource cleanup with finally
# try ... finally
# lets you clean up whether an exception occurs or not
# the next code will be executed, even the previous code
# interrupt


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
        # if try block crash
        # the finally still run
    finally:
        # finally: block runs even the aboves blocks don't
        os.chdir(original_path)
# errors should never pass silently
# unles explicitly silenced
# platform-specific modules
# windows msvcrt
# linux  osx : sys, tty, termios
