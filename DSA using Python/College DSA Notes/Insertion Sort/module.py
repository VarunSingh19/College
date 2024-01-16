def insertion_sort(newlist):
    for i in range (1,len(newlist)):
        value = newlist[i]
        j = i-1
        while j>=0 and value < newlist[j]:
            newlist[j+1] = newlist[j]
            j-=1
        newlist[j+1]=value
    return newlist

newlist = [45,64,2,-1,-32]
print("The Unsorted list is :", newlist)
print("The Sorted list is :", insertion_sort(newlist))