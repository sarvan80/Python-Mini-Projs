'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)


def update(data):
    line.set_ydata(data)
    return line,


def data_gen():
    while True:
        yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()
'''
from mySearches import Sorts, bisearch, lsearch
infile = 'rands.txt'
f = open(infile,'r')
data = f.read()
f.close()

#Cleaning up the list
data = data.replace('\n','\t')
data = data.split('\t')

#t=len(data)
#print(t)
'''
#Converting and storing the list as Integers
Intlist = []
for i in data:
    Intlist.append(int(i))
'''

#Converting and storing the list as Integers
Index = []
for i in range(0,10000):
    Index.append(int(i))

#Converting the unsorted numbers to numeric value
Integer = map(int,data)
unsort=Integer
print Index
print Integer
print len(Integer)
print unsort

import matplotlib.pyplot as plt
import numpy as np

x = np.array(Index)
y = np.array(Integer)
z = np.array(Sorts(Integer))

print x
print len(x)
print len(y)
print len(z)
#Sorting the numbers in the list

#S=Sorts(Integer)
'''
print Sorts(Integer)


print(data)
print S
print US
print len(US)
'''

import matplotlib.pyplot as plt

plt.plot(x, y, x, z)#Plotting  Sorted & Unsorted numbers along the index
plt.ylabel('sorted & Unsorted')
plt.show()

