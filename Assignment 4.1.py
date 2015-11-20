
#####################Question#############
# MyList = [ 23, 45, 6, 23, -9, 77, 54, -54, 21, 2, 8, -3, 23, 45, 93, -43, 999, -2, 3, 78, 90 ]
 
# Given the list above write a program that prints out the average of the non-negative numbers in 
# the list before the value 999. 

############# LOGICAL CONSTRUCT ###########
# Define the list and iterate the elements using For loop to find the mean
# using the counters A for Sum and K for count,after checking for non-negetivity
# and range(<999).The Mean is then calculated outside the loop using the formula 
# A(sum)/K(Count)


########## Critical Aspect #################
# Having counters for both the sum and the float and increment them only when the 
# condition is satisfied and when the numbers are with in the boundry
# Conversion of result to float

##########  PROGRAM ########################
# List Definition
	
'''
MyList = [ 23, 45, 6, 23, -9, 77, 54, -54, 21, 2, 8, -3, 23, 45, 93, -43, 999, -2, 3, 78, 90 ]
# List to check the Logic MyList = [ 2,2,2,2,999,-2,0]

# Counter Initialization
a=0
k=0

# Iterating for finding the mean
for i in MyList:

# Checking for non-Zero and <999 conditionalities
	if(i>=0):
		if(i<999):
			a=a+1
			k=k+i

# Float point conversion of the result for Accuracy			
Av = float(k)/float(a)

# Printing the Result
print('The Average of the non zero numbers less than 999 in List is',Av)
			
torial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

y=factorial(8)
print y
'''
# this is a comment
#
# Author Lars
#
#  A program to do a binary search on a list of numbers
#

def bsearch(x, nums):
    item =0
    low = 0
    high = len(nums) -1
    c = 0

    while low <= high:                   # Still a range to search
        print("Step counter : ",c,item)
        mid = (low+high)//2              # this is the position of the middle number
        item = nums[mid]
        print("The Mid:",item)

        if x == item:        # got it, now return it!
            return mid

        elif x < item:       # x is in the lower half of the range
            high = mid -1    #    move the top marker down
            c = c + 1        #    up the step counter

        else:                # x is in the upper half
            low = mid + 1    #    move the bottom marker up
            c = c + 1        #    up the step counter
    return -1                # x is not found


MyNums = list(range(1,1000000))
# print(MyNums[4])

x = bsearch(4,MyNums)
print(x)
print("The number is found! : ", MyNums[x])

# My program starts here#


infile = 'rands.txt'
f = open(infile,'r')
data = f.read()
f.close()
data = data.replace('\n','\t')
data = data.split('\t')
print(data)
t=len(data)
print(t)

#Converting and storing the list as Integers
Intlist = []
for i in data:
    Intlist.append(int(i))
#print Intlist

# Sorting the numbers in the list
def Sorts(Inlist):
    for k in range(1,len(Inlist)):
        for j in range(k+1,len(Inlist)):
   
            if Inlist[j]<Inlist[k]:

                Inlist[k],Inlist[j]=Inlist[j],Inlist[k]
    return Inlist
#Sorting Algorithm
#Strong in coding &
# which brackets the use
# spliting the 100 hrs i have got in coding & tech
# get the rough locic;pseudo coding ;coding in fav ;fig out best to use;
# Actual Coding
S=Sorts(Intlist)
print S

Index=bsearch(1,S)
print Index
'''
print data
print len(data)
i=0 

for i in data:


	print i
# Con_data

l=len(data)
print l
for i in data:
	print i
print len(data)

# Converting string to integer

'''

