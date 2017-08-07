my_list = []
for i in range(1, 10):
    my_list.append(i)

print my_list

my_var = my_list[4] + my_list[5]
print "my_var = ", my_var

import numpy as np # an elision

# create list of Celsius temps
templist = [25.3, 24.8, 26.9, 23.9]
# create numpy array
temparray = np.array(templist)
# convert to Fahrenheit
flist = [ x*9/5 + 32 for x in templist]
farray = temparray * 1.8 + 32

print flist
print farray
'''
NumPy supports large, multi-dimensional arrays and matrices and a large collection of mathematical functions
to operate on them, like trig, arithmatic, exp, log, etc.
an advantage of numpy vs. python list is the use of vectorized operations in numpy
vectorized operations is a term referring to the application of a command to every element of a array
List pros: general-purpose containers; insertion, deletion, appending, and concatenation
Cons: does not support vectorized operations; can contain objects of differing types,
so that  type information must be stored for every element and programmed for when operating on each element.
'''
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
my_var =  11
[77.54, 76.64, 80.42, 75.02]
[ 77.54  76.64  80.42  75.02]
'''



