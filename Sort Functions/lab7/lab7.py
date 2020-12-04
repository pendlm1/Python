#Mario Pendleton
#cs303
#lab1

from time import*
import random
import sys
from statistics import*

def load (path):
    lst=[]
    file = open(path)
    strList = file.read().split()
    for i in strList:
        i = int(i)
        lst.append(i)
    file.close()
    return lst

def loadLine (path):
    lst=[]
    file = open(path)
    for line in file:
        if line != "\n":
            lst.append(line.split())
    file.close()
    return lst

def sampleList (n):
    sample = []
    k = 0
    for i in range(2**n):
        k = random.randint(0,2**n)
        sample.append(k)
    end = process_time()

    return sample
######################## Linear Serach ##############################
def linearSearch (x,y):
    start = process_time()
    l = []
    key = 0
    print('\n Printing linear search results...\n')
    for i in range(len(x)):
        key = x[i]
        for j in range(len(y)):
            if key == y[j]:
                l.append(key)
    print(l)
    end = process_time()
    print('\n Linear Search | Start:',start, ",", 'End:',end,'| Linear Search completed in:',end-start)

######################## Bibnary Search ##############################
def iterateKeys(x,y,l,r):
    key = 0
    for i in range(len(x)):
        key = x[i]
        binarySearch(key,y,l,r)
    return     
 
def binarySearch(k,y,l,r):
    m = 0
    if l != r:
        return True
    else:
        m = (r+l)//2
        
    if k > y[m]:
        r=y[m:len(y)]
        print(k,r[m])
        return binarySearch(k,y,l,r[m-1])

    if k < y[m]:
        l=y[0:m+1]
        print(k,l[m])
        return binarySearch(k,y,l,r)

######################## Insertion Sort ##############################
def insertionSort(list):
    
    key = 0
    for j in range(1,len(list)):
        key = list[j]
        i = j-1
        while i>=0 and list[i]< key:
            list[i+1] = list[i]
            i = i-1
            list[i+1] = key
######################## Merge Sort ##############################
def mergeSort(x,y,l,r):
    
    if l<r:
        m = (l+r)//2

        mergeSort(x,y,l,m)
        mergeSort(x,y,m+1,r)
        merge(x,y,l,m,r)


def merge(x,y,l,m,r):
    i = l
    j = m+1
    y = x[:]

    for k in range(l,r+1):
        if i > m:
            x[k] = y[j]
            j=j+1

        elif j > r:
            x[k] = y[i]
            i = i+1

        elif y[j] > y[i]:
            x[k] = y[j]
            j = j+1

        else:
            x[k] = y[i]
            i = i+1
######################## Heap Sort ##############################
def heapSort(x):
    heapSize = len(x)

    for i in range(heapSize//2,-1,-1):
        maxHeapify(x,heapSize,i)
    
    for i in range(heapSize-1,0,-1):
        x[i],x[0] = x[0],x[i]
        maxHeapify(x,i,0)

def maxHeapify(x, heapSize, i):
    l = 2*i+1
    r = 2*i+2

    if l < heapSize and x[l] < x[i]:
        largest = l
    else:
        largest = i

    if r < heapSize and x[r] < x[largest]:
        largest = r

    if largest != i:
        x[i],x[largest] = x[largest],x[i]
        maxHeapify(x,heapSize,largest)

######################## Quick Sort ##############################
def quickSort(x,l,r):
    if l < r:
        p = partition(x,l,r)
        qSort(x,l,p-1)
        qSort(x,l+1,r)

def partition(x,l,r):
    k = x[r]
    i = l-1
    
    for j in range(l,r):
        if x[j] >= k:
            i = i+1
            x[i],x[j] = x[j],x[i]
    x[i+1],x[r] = x[r],x[i+1]
    return i+1
    
def qSort(x,l,r):
    if l<r:
        n = r-l+1
        m = median3(x,l,l+n//2,r)
        x[m],x[r] = x[r],x[m]
        p = partition(x,l,r)
        qSort(x,l,p-1)
        qSort(x,p+1,r)

def median3(x,i,j,k):
    m = [x[i],x[j],x[k]]
    med = median(m)
    if med == x[i]:
        return i
    elif med == x[k]:
        return k
    else:
        return j
    
######################## Max/Min Sort ##############################
def mySort(x,l,r):
    while l<=r:
        MaxMinSort(x,l,r)
        l = l+1
        r = r-1

def MaxMinSort(x,l,r):
    i = l
    max = x[l]
    min = x[l]
    
    while i <= r:
        if x[i] <= max:
            max = x[i]
            maxp = i
        if x[i] >= min:
            min = x[i]
            minp = i
        i = i+1

    x[l],x[minp] = x[minp],x[l]
    x[r],x[maxp] = x[maxp],x[r]
    
######################## Bubble Sort ##############################
def bubbleSort(x):
    for i in range(1 ,len(x)-1):
        for j in range (1,len(x)-i+1):
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1],x[j]
        
######################## Reverse Bubble Sort ##############################
def revBubbleSort(x):
    for i in range(1 ,len(x)-1):
        for j in range (1,len(x)-i+1):
            if x[j] > x[j-1]:
                x[j], x[j-1] = x[j-1],x[j]

######################## Selection Sort ##############################
def selectionSort(x):
    for i in range(0,len(x)-1):
        min = i
        for j in range(i+1,len(x)):
            if x[j] < x[min]:
                min = j
        if i != min:
            x[min],x[i] = x[i],x[min]
        

######################## Reverse Selection Sort ##############################
def revSelectionSort(x):
    for i in range(0,len(x)-1):
        min = i
        for j in range(i+1,len(x)):
            if x[j] > x[min]:
                min = j
        if i != min:
            x[min],x[i] = x[i],x[min]
                
######################## Start Timer ##############################

start = process_time()
print('\n###############################################################################')

##################################### Enter Prams Here #######################################
n = 3 #Use n to create a random array of n**2 in size
s = 10000

#path2 = "NovelSortInput.txt"
path = "input_100.txt"
#path = "input_1000.txt"
#path = "input_5000.txt"
#path = "input_10000.txt"
#path = "input_50000.txt"
#path = "input_100000.txt"
#path = "input_500000.txt"
#path = "Input_Sorted.txt"
#path = "input_ReversedSorted.txt"
#path = "Input_Random.txt"

a = ["apple", "cherry", "mango", "banana", "dragon fruit"]
b = [123,"apple",5,6,"green"] #Expected crash
c = ["123", "apple","5","53","5a","6","green"]
d = [10.1,10.9,9.3,7.4,6.49,2.0,1.999,0.01,5.999]
e = sampleList(n)
f = load(path)
g = []
h = [13]
i = ["red"]
j = [-245,245,-1,1,0,45,-45,2,-2,3,-3]
k = [6,4,8,10,2,99,77,68,53]

#temp = a
#temp = b
#temp = c
#temp = d
#temp = e
#temp = f
#temp = g
#temp = h
#temp = i
#temp = j
#temp = k
################################## Function Calls ###################################
insertionSort(a)
print("Reverse Inserion Sort results:\n",a)

mergeSort(c,[],0,len(c)-1)
print("Reverse Merge Sort results:\n",c)

heapSort(d)
print("Reverse Heap Sort results:\n",d)

quickSort(e,0,len(e)-1)
print("Reverse Quick Sort results:\n",e)

mySort(f,0,len(f)-1)
print("Reverse Max/Min Sort results:\n",f)

bubbleSort(g)
print("Bubble Sort results:\n",g)

revBubbleSort(h)
print("Reverse Bubble Sort results:\n",h)

selectionSort(i)
print("Selection Sort results:\n",i)

revSelectionSort(j)
print("Reverse Selection Sort results:\n",j)


######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")
