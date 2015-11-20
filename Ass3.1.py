sumdigit(a)
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

y=sumdigit(234)
print(y)