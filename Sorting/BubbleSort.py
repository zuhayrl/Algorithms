# BUBBLE SORT
#Best case: n   Worst Case: n^2     Average Case n^2
import random

#Sort Algorithm =======================================================================
def bubbleSort(list):
    #loop through each item
    for i in range(len(list)):
        #loop to compare items
        for j in range(0,len(list)-i-1):
            #check if >
            if list[j]>list[j+1]:
                #Swap if true
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    
    return list
#======================================================================================

#Create Data
data = []
for i in range(0,20):
    data.append(random.randint(1,100))


#Check Sort
print("Original List")
print(data)
print("\nSorted Lists")
print(bubbleSort(data))
