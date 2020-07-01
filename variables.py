#!/usr/bin/env python3


# this is an updated version of this progran sent to github.com/GitExample3/Version2
# variables
# begins with a character or single underscore
# case sensitive
# no spaces
# can't begin w/ a number
# can't be a reserved word
# 'a' is being assigned, is a pointer, for the value of 1 in memory
# 'a' is a tag for what is a memory location
a = 1
# print location in memory
print(id(a))
_a = 2
print(id(_a))
# python3, then type dir() to see variables in your name space
#
# these are different variables
number10 = 10
Number20 = 20
NumBer30 = 30
NUMBer40 = 40
print('{0} {1} {2} {3}'.format(number10, Number20, NumBer30, NUMBer40))
#
# camel casing = numAddresses, numRouters > both upper and lower case variables
#
# to delete a variable > del(nubmer10)
#
a = 10
b = 20
c = 30
print('{0} {1} {2}'.format(a, b, c))
print(id(a), id(b), id(c))
# a is assigned the value in memory that c points to
a = c
# a now points to the same place in memory as c
print('{0} {1} {2}'.format(a, b, c))
print(id(a), id(b), id(c))
