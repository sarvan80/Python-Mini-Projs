
from mySearches import Sorts, bisearch, lsearch
infile = 'rands.txt'
f = open(infile,'r')
data = f.read()
f.close()

#Cleaning up the list
data = data.replace('\n','\t')
data = data.split('\t')
print(data)
#t=len(data)
#print(t)

#Converting and storing the list as Integers
Intlist = []
for i in data:
    Intlist.append(int(i))

#Sorting the numbers in the list
S=Sorts(Intlist)
print S

Item=bisearch(78700,S)
Item=lsearch(78700,S)
Item=bisearch(3333,S)
Item=lsearch(3333,S)
Item=bisearch(1118,S)
Item=lsearch(11118,S)





