
# Function to calculate the sum
def sumdigit(a):
	# a=234477
	mystr = str(a)
	x=len(mystr)

	z=0
	for i in range(1,x):
		y=mystr[i:i+1]
		z=int(y)+z
	sum=z+int(mystr[:1])
	# print(sum)
	return sum
# Function to calculate whether the number is HArshad or not
def isHarshad(a):
	s=sumdigit(a)
	# print(s)
	if(a%s==0):
		return True
	else:
		return False

# Printing the list of Harshad numbers from 1 to 500
Mylist = [ ]
for i in range(1,500):
	y=isHarshad(i)
	if(y==True):
		Mylist.append(i)
print(Mylist)





