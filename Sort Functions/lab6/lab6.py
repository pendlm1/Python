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

def iterateKeys(x,y,l,r):
    start = process_time()
    key = 0
    for i in range(len(x)):
        key = x[i]
        binarySearch(key,y,l,r)
    end = process_time()
    print('\n Binary key iterator Search | Start:',start, ",", 'End:',end,'| Binary key iterator completed in:',end-start)
    print(y)
    return     
 
def binarySearch(k,y,l,r):
    start = process_time()
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
    end = process_time()
    print('\n Binary Search | Start:',start, ",", 'End:',end,'| Binary Search completed in:',end-start)

def insertionSort(list):
    
    key = 0
    for j in range(1,len(list)):
        key = list[j]
        i = j-1
        while i>=0 and list[i]> key:
            list[i+1] = list[i]
            i = i-1
            list[i+1] = key

def mergeSort(x,y,l,r,s):

    if len(x)<=s:
        insertionSort(x)
    
    elif l<r:
        m = (l+r)//2

        mergeSort(x,y,l,m,s)
        mergeSort(x,y,m+1,r,s)
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

        elif y[j] < y[i]:
            x[k] = y[j]
            j = j+1

        else:
            x[k] = y[i]
            i = i+1

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

    if l < heapSize and x[l] > x[i]:
        largest = l
    else:
        largest = i

    if r < heapSize and x[r] > x[largest]:
        largest = r

    if largest != i:
        x[i],x[largest] = x[largest],x[i]
        maxHeapify(x,heapSize,largest)

def QuickSort(x,l,r):
    if l < r:
        p = partition(x,l,r)
        QSort(x,l,p-1)
        QSort(x,l+1,r)

def partition(x,l,r):
    k = x[r]
    i = l-1
    
    for j in range(l,r):
        if x[j] <= k:
            i = i+1
            x[i],x[j] = x[j],x[i]
    x[i+1],x[r] = x[r],x[i+1]
    return i+1
    
def QSort(x,l,r):
    if l<r:
        n = r-l+1
        m = median3(x,l,l+n//2,r)
        x[m],x[r] = x[r],x[m]
        p = partition(x,l,r)
        QSort(x,l,p-1)
        QSort(x,p+1,r)

def median3(x,i,j,k):
    m = [x[i],x[j],x[k]]
    med = median(m)
    if med == x[i]:
        return i
    elif med == x[k]:
        return k
    else:
        return j
    
    
 ######################## mySort ##############################

def mySort(x,l,r):
    while l <= r:
        MaxMinSort(x,l,r)
        l = l+1
        r = r-1

def MaxMinSort(x,l,r):
    i = l
    max = x[l]
    maxp = x[l]
    min = x[l]
    minp = x[l]
    
    while i <= r:
        if x[i] >= max:
            max = x[i]
            maxp = i
        if x[i] <= min:
            min = x[i]
            minp = i
        i = i+1

    x[l],x[minp] = x[minp],x[l]
    x[r],x[maxp] = x[maxp],x[r]
    

    
    


    
####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')

##################################### Enter Prams Here #######################################
n = 3 #Use n to create a random array of n**2 in size
s = 10000

path2 = "NovelSortInput.txt"
path = "input_100.txt"
#path = "input_1000.txt"
#path = "input_5000.txt"
#path = "input_10000.txt"
#path = "input_50000.txt"
#path = "input_100000.txt"
#path = "input_500000.txt"

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
l = f2 = loadLine(path2)


####################################### Function Calls #######################################
mySort(a,0,len(a)-1)
print("Max/Min sort results\n",a)
print('\n###############################################################################')
#mySort(b,0,len(b)-1)
#print("Max/Min sort results\m",b)
print('\n###############################################################################')
mySort(c,0,len(c)-1)
print("Max/Min sort results\n",c)
print('\n###############################################################################')
mySort(d,0,len(d)-1)
print("Max/Min sort results\n",d)
print('\n###############################################################################')
mySort(e,0,len(e)-1)
print("Max/Min sort results\n",e)
print('\n###############################################################################')
mySort(f,0,len(f)-1)
print("Max/Min sort results\n",f)
print('\n###############################################################################')
mySort(g,0,len(g)-1)
print("Max/Min sort results\n",g)
print('\n###############################################################################')
mySort(h,0,len(h)-1)
print("Max/Min sort results\n",h)
print('\n###############################################################################')
mySort(i,0,len(i)-1)
print("Max/Min sort results\n",i)
print('\n###############################################################################')
mySort(j,0,len(j)-1)
print("Max/Min sort results\n",j)
print('\n###############################################################################')
mySort(k,0,len(k)-1)
print("Max/Min sort results\n",k)
print('\n###############################################################################')
mySort(l,0,len(l)-1)
print("Max/Min sort results\n",l)




########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")
