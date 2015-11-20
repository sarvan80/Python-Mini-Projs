
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
			
			




