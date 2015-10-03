import re

# http://code.activestate.com/recipes/135435-sort-a-string-using-numeric-order/
def stringSplitByNumbers(x):
    r = re.compile('(\d+)')
    l = r.split(x.lower())
    return [toNumber(y) if y.isdigit() else y for y in l]

def toNumber(y):
    try:
        return int(y)
    except:
        return long(y) # python 2
