# Plotting Rands sorted and unsorted vs Index
#
# Author : Saravanan-Assignment 3 module 4 Class Python(Prof.Lars)


from mySearches import Sorts, bisearch, lsearch
infile = 'rands.txt'
f = open(infile,'r')
data = f.read()
f.close()

#Cleaning up the list
data = data.replace('\n','\t')
data = data.split('\t')
#Converting and storing the list as Integers
Index = []
for i in range(0,10000):
    Index.append(int(i))
#Converting the unsorted numbers to numeric value
Integer = map(int,data)

#Importing the Matplotlib Libraries
import matplotlib.pyplot as plt
import numpy as np

x = np.array(Index)
y = np.array(Integer)
z = np.array(Sorts(Integer))

import matplotlib.pyplot as plt

plt.plot(x, y,'g^', x, z,'bs')#Plotting  Sorted & Unsorted numbers along the index
plt.ylabel('sorted & Unsorted')
plt.show()