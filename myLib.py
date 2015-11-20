# Function to calculate the sum of the digit called by isHarshad
# Is not required in Question;created for my convenience(Professor please
# let me know if its not ok I will re-program)
def sumdigit(a):
	# a=234477
	mystr = str(a)
	x=len(mystr)

	z=0
	for i in range(1,x):
		y=mystr[i:i+1]
		z=int(y)+z
	sum=z+int(mystr[:1])# Sum of the digits of the number
	# print(sum)
	return sum
#Function to check if the number is Harshad or not
def isHarshad(a):
	s=sumdigit(a)
	# print(s)
	if(a%s==0):
		return True
	else:
		return False
#Function to check if the Harshad number has 7 in the Ten's digit
def isSiete(a):
	# s=sumdigit(a)
	# print(s)
	if(a > 10):
		l1=str(a)
		c=int(l1[len(l1)-2:-1])#Getting the Ten's digit of the number
		if(c==7):
			return True
		else:
			return False
Seaver=41