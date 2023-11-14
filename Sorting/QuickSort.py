# QUICK SORT
#Best case: nlogn   Worst Case: n^2
import random

#Sort Algorithm =======================================================================
def quicksort(list):
    #check if only one element or empty
    if len(list) <= 1:
        return list

    #Define Pivot and lesser and greater arrays
    pivot_index = len(list)-1
    pivot = list[pivot_index]
    
    greater = []
    lesser = []

    #sort
    for i in range(0,pivot_index):
        if (list[i] > pivot):
            greater.append(list[i])
        else:
            lesser.append(list[i])

    return (quicksort(lesser)+ [pivot] + quicksort(greater))
#======================================================================================

#Create Data
data = []
for i in range(0,10):
    data.append(random.randint(1,100))


#Check Sort
print("Original List")
print(data)
print("\nSorted Lists")
print(quicksort(data))


