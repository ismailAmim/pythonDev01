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


def convert_w_h(s):
    ''' testing '''
    try:
        x = int(s)
        print(" conversion succeeded !")
    except ValueError:
        x = -1
        print(" conversion failed ???!")
    except TypeError:
        x = -1
        print(" conversion failed ???!")
    return x


print(convert_w_h("15"))
print(convert_w_h("bob"))
