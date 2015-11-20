##################PROG 5#################
#
#
#
#
'''
import Tools
def isPal(thestr):
    if thestr == thestr[::-1]:
        return True
    else:
        return False

Hodges = 14
'''
from Tools import isPal, Hodges
# Open file, read data, close file
infile = 'rnums.txt'
f = open(infile,'r')
data = f.read()
# print(data)
data=data.split('\n')
f.close()


# iterate through the list and find the palindromes
for i in data:
    if isPal(i) == True:
        print(i)
print('\n')
print(Hodges)
# this is a comment
#
# Author : Lars
#
# library for palindrome prog


