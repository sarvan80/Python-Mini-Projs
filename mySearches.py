
# Professor I used your bsearch program for the binary search
# Do let me know if I have to code it up on my own

def bisearch(x,nums):
    
    item =0
    low = 0
    high = len(nums) -1
    c = 0

    while low <= high:                   # Still a range to search
        #print("Step counter : ",c,item)
        mid = (low+high)//2              # this is the position of the middle number
        item = nums[mid]
        #print("The Mid:",item)

        if x == item:        # got it, now return it!
            print("Item",x,"is found by binary search and the index is:",mid)
            print("Number of lookups for binary search:",c)
            return mid

        elif x < item:       # x is in the lower half of the range
            high = mid -1    #    move the top marker down
            c = c + 1        #    up the step counter

        else:                # x is in the upper half
            low = mid + 1    #    move the bottom marker up
            c = c + 1
    print("Number not found")
    print("Number of lookups in binary search:",c)        #    up the step counter
    return -1                # x is not found


def lsearch(x,nums):
    # item =0
    # low = 0
    # high = len(nums) -1
    c = 0
    for k in range(1,len(nums)-1):
        c=c+1
        #print nums[k]
        if x == nums[k]:
            print("Item",x,"is found by linear search and the index is:",k)
            print("Number of lookups for linear search:",c)
            return k
    print("Number not found")
    print("Number of lookups in linear search:",c) 
    return -1


def Sorts(Inlist):
    for k in range(0,len(Inlist)-1):
        for j in range(k+1,len(Inlist)):
   
            if Inlist[j]<Inlist[k]:

                Inlist[k],Inlist[j]=Inlist[j],Inlist[k]
    return Inlist

