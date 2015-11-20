#  This is still a comment
#
# Author : Lars
#
# implement multiplication recursively

def mult(num, times):
    if times == 1:
        return num
    else:
        return num + mult(num, times-1)

# main
a = mult(7,3)
print(a)

b = mult(8,23)
print(b)
