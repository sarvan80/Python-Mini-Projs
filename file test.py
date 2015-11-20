##################PROG 5#################
#
#
#
#

# import Tools
def isPal(thestr):
    if thestr == thestr[::-1]:
        return True
    else:
        return False

Hodges = 14

# Open file, read data, close file
infile = 'rnums.txt'
f = open(infile,'r')
data = f.read()
# print(data)
f.close()


# iterate through the list and find the palindromes
for i in data:
    if isPal(i) == True:
        print(i)
# print(Hodges)
# this is a comment
#
# Author : Lars
#
# library for palindrome prog

