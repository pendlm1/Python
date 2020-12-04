#Mario Pendleton
#cs303
#lab1

from time import*
import random
import sys

def load (path):
    #start = process_time()
    lst=[]
    file = open(path)
    strList = file.read().split()
    for i in strList:
        i = int(i)
        lst.append(i)
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


''' Heap sort starts here'''######################## Heap Sort ##############################

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



####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')

##################################### Enter Prams Here #######################################
n = 3 #Use n to create a random array of n**2 in size
s = 10000
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
example = [6,4,8,10,2]

####################################### Function Calls #######################################
heapSort(a)
print("Heap sort results: \n",a)

#heapSort(b)
#print("Heap sort results: \n",b)

heapSort(c)
print("Heap sort results: \n",c)

heapSort(d)
print("Heap sort results: \n",d)

heapSort(e)
print("Heap sort results: \n",e)

heapSort(f)
print("Heap sort results: \n",f)

heapSort(g)
print("Heap sort results: \n",g)

heapSort(h)
print("Heap sort results: \n",h)

heapSort(i)
print("Heap sort results: \n",i)

heapSort(j)
print("Heap sort results: \n",j)

########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")
