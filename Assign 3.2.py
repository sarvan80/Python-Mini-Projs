from myLib import sumdigit, isHarshad, isSiete, Seaver
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
# List reation for the Harshed Numbers
Mylist = [ ]
for i in data:
	y=isHarshad(int(i))
	if(y==True):
		Mylist.append(i)
print(Mylist)# List of Harshed numbers 
t1=len(Mylist)
print(t1)
sum2=sum1(Mylist)
print(sum2)

MySelect = [ ]
for j in Mylist:
	z=isSiete(int(j))
	if(z==True):
		MySelect.append(j)
print(MySelect)# List of Harshed numbers having 7 in the ten's digit
t2=len(MySelect)
print(t2)
sum3=sum1(MySelect)
print(sum3)
# Writing the numbers having 7 in the ten's digit in the file
offile = "Harshout.txt"
outf = open(offile,"w")

for i1 in MySelect:
	l1=str(i1)
	# print(l1)
	outf.write("%s\n" % l1)

MyFinalSelect = [ ]
for k in MySelect:
	if(int(k)%Seaver==0):
		d=int(k)/Seaver
		if(d%2==0):
			MyFinalSelect.append(k)
print(MyFinalSelect)# List of Harshed numbers having 7 in the ten's digit & evenly divisible by 41
t3=len(MyFinalSelect)
print(t3)
sum4=sum1(MyFinalSelect)
print(sum4)

# Writing the sum of the Harshad numbers in the Rumbers file
f = open('Rumbers.txt', 'a')
f.write('\n')
# f.write('\n')
f.write(str(sum2))
f.close()