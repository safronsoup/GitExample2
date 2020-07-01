#!/usr/bin/env python3

# integer can't be changed in place - immutable - if assigned value changes,
# the memory location changes
# positive or negative whole numbers
#
# int class from which data types interger are created
# int() function that allows other data types to be converted to interger
#
posNumber = 99
strNumber ='99'
print(posNumber, type(posNumber), id(posNumber))
print(strNumber, type(strNumber), id(strNumber))
posNumber = 22
print(posNumber, type(posNumber), id(posNumber))
#
posNum = int(strNumber)
print(posNum, type(posNum))
#
#
print(9 + 9)
# return a float number
division = 10 / 5
print(division, type(division))
# return an integer
division2 = 10 // 5
print(division2, type(division2))
#
# truncate everything after the decimal
floatnum =3.78888
print(int(floatnum), type(floatnum))
