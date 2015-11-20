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

def isHarshad(a):
	s=sumdigit(a)
	# print(s)
	if(a%s==0):
		return True
	else:
		return False

def isSiete(a):
	# s=sumdigit(a)
	# print(s)
	if(a > 10):
		l1=str(a)
		c=int(l1[len(l1)-2:-1])
		if(c==7):
			return True
		else:
			return False
# Open file, read data, close file
# Converting the number to List
infile = 'Rumbers.txt'
f = open(infile,'r')
data = f.read()
f.close()

# prepare our data
data = data.replace('\n','\t')
data = data.split('\t')
print(data)
t=len(data)
print(t)

# sum of numbers
def sum1(list1):
	s=0
	for i in list1:
		s=s+int(i)
	return s
'''
def Selectivelist(list1)
	newlist = [ ]
	for i in list1:
		c=int(mystr[len(list1)-2:-1])
		if(c==7):
			newlist.append(i)
	print(newlist)
# List
'''
Mylist = [ ]
for i in data:
	y=isHarshad(int(i))
	if(y==True):
		Mylist.append(i)
print(Mylist)
t1=len(Mylist)
print(t1)
sum2=sum1(Mylist)
print(sum2)

MySelect = [ ]
for j in Mylist:
	z=isSiete(int(j))
	if(z==True):
		MySelect.append(j)
print(MySelect)
t2=len(MySelect)
print(t2)
sum3=sum1(MySelect)
print(sum3)

offile = "Harshout1.txt"
outf = open(offile,"w")

for i1 in MySelect:
	l1=str(i1)
	# print(l1)
	outf.write("%s\n" % l1)

MyFinalSelect = [ ]
for k in MySelect:
	if(int(k)%41==0):
		d=int(k)/41
		if(d%2==0):
			MyFinalSelect.append(k)
print(MyFinalSelect)
t3=len(MyFinalSelect)
print(t3)
sum4=sum1(MyFinalSelect)
print(sum4)

# Writing the sum of the Harshad numbers in the Rumbers file
f = open('Rumbers1.txt', 'a')
f.write('\n')
# f.write('\n')
f.write(str(sum2))
f.close()



