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
    #end = process_time()
    #print('\n Loading Data | Start:',start, ",", 'End:',end,'| Data Loaded in:',end-start)
    return lst

def sampleList (n):
    #start = process_time()
    sample = []
    k = 0
    for i in range(2**n):
        k = random.randint(0,2**n)
        sample.append(k)
    end = process_time()
    #print('RD',sample)
    #print('\n Random Data | Start:',start, ",", 'End:',end,'| Random data generated in:',end-start)
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
    return

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
    testData = list[:]
    
    print("Original array:\n", list)
    key = 0
    for j in range(1,len(list)):
        key = list[j]
        i = j-1
        while i>=0 and list[i]> key:
            list[i+1] = list[i]
            i = i-1
            list[i+1] = key
    print ("Insertion sort results:\n",list)
    testData.sort()
    if testData == list:
        print("Insertion sort was successful. No errors found.")
        return True
    else:
        print("Insetion sort failed. Review the arrays for errors. \n","Python sort \n",testData)
        return False       

####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')

##################################### Enter Prams Here #######################################
n = 3 #Use n to creat a random array of n**2 in size
path = "input_100.txt"
#path = "input_1000.txt"
#path = "input_5000.txt"
#path = "input_10000.txt"
#path = "input_50000.txt"
#path = "input_100000.txt"
#path = "input_500000.txt"



a = ["apple", "cherry", "mango", "banana", "dragon fruit"]
b = [123,"apple",5,6,"green"] #Expected crash
c= ["123", "apple","5","53","5a","6","green"]
d = [10.1,10.9,9.3,7.4,6.49,2.0,1.999,0.01,5.999]
e = sampleList(n)
f = load(path)
g = []
h = [13]
k = ["red"]

####################################### Function Calls #######################################
print(insertionSort(a))
#print(insertionSort(b)) #Expected crash
print(insertionSort(c))
print(insertionSort(d))
print(insertionSort(e))
print(insertionSort(f)) # for txt files, alter path= for different results
print(insertionSort(g))
print(insertionSort(h))
print(insertionSort(k))

########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")

