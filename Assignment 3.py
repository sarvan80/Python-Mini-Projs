   
# List & For Loops
# Assignment 3

'''
for i in range(1,301):
   
   if(i % 26 == 0):
   
		print(i)

list=[]

for i in range(1,100):
	
   
	if(i % 3 == 0):
		print("Cow")
		k=i*24
 	
		list.append(k)
   
print(list)
print(k)
print(i)

'''
# need for a return statement?

# Assignment CowPie
# list=[]
'''
############# LOGICAL CONSTRUCT ###########
# Make an array of 100 elements#
# Check for divisibility with 3 and if the condition is satisfied make a sub-block to#
# check for divisibility if both conditions are satisfied print "CowPie" or if only one condition #
# is Satisfied type "Cow".IF the condition fails for 3 check for divisibility with 7 and #
# if that is satisfied type "Pie"(Here we dont have to check again for divisibility with 3#
# since that condition is already failed.If both the Main conditions ie divisibility with#
# 3 and 7 fail print the number#

########## Critical Aspect #################
# Avoid Rule clash on numbers which are divisible by 7 & 3 and keep the rules #
# Mutually exclusive ie any point in time only one rule is satisfied#


# Block to Initialize the Array to check the divisibility condition #

for i in range(1,100):
	
 # checking for both 3 & 7  
	if(i % 3 == 0):
	
	#Sub block to check divisibility with 7
		if(i % 7 == 0):
			print("CowPie")
		else:
			print("Cow")
	# Rule to check 7 only Divisibility
	elif(i % 7 == 0):
			print("Pie")						
    # Printing number on both rules not satisfied
	else:
		print(i)
   	
'''
# MyList = [ 23, 45, 6, 23, -9, 77, 54, -54, 21, 2, 8, -3, 23, 45, 93, -43, 999, -2, 3, 78, 90 ]
 
# Given the list above write a program that prints out the average of the non-negative numbers in 
# the list before the value 999. 

############# LOGICAL CONSTRUCT ###########

########## Critical Aspect #################
# Having counters for both the sum and the float and increment them only when the 
# condition is satisfied and when the numbers are with in the boundry
# Conversion of result to float

# List Definition

MyList = [ 23, 45, 6, 23, -9, 77, 54, -54, 21, 2, 8, -3, 23, 45, 93, -43, 999, -2, 3, 78, 90 ]
# MyList = [ 2,2,2,2,999,-2,0]

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
print('The Sum of the non zero numbers less than 999 in List is',Av)
			
			




