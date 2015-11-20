#  This is still a comment
#
# Author : Saravanan-Powered by Prof.Lars code on Multiplication
#
# implement Power recursively

def myPow(num, times):
    if times == 1:
        return num
    else:
        return num*myPow(num, times-1)

# main
a = myPow(7,3)
print(a)

b = myPow(2,6)
print(b)

c = myPow(4,2)
print(c)

