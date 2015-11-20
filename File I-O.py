'''
#################PROG 4#################
#
# This is a comment
# A:Lars
#

infile = "mynums.txt"
offile = "outnums.txt"
outf = open(offile,"w")

accum = 0
with open(infile,"r") as f:
    for line in f:
        num = int(line)
        accum = accum + num 
        outf.write(str(num+1)+'\n')

print("The sum is", accum)
outf.close()

def cube(x): 
	answer = x*x*x 
	return(answer) 

# use cube 
answer = 4 
result = cube(3) 
print(answer, result)

import numpy as np
def root(x,y): 
# i=y
	for i in np.arange(1,x,1):
		j=y
		A=x
		while j>1:	
			j=j-1
			A=A/i
		if A==i:
			Ans=A
			return(Ans) 

# use cube 
# answer = 4 
result = root(64,6) 
print(result)
'''
def root(x,y)
import numpy as np
def root(x,y): 
# i=y
	for i in range(1,x):
		A=x
		for j in range(1,y):
			A=A*j
			
		if A==i:
			Ans=A
			return(Ans) 

# use cube 
# answer = 4 
result = root(8,3) 
print(result)
