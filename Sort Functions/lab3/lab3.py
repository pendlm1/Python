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
    #testData = list[:]
    
    key = 0
    for j in range(1,len(list)):
        key = list[j]
        i = j-1
        while i>=0 and list[i]> key:
            list[i+1] = list[i]
            i = i-1
            list[i+1] = key
#print ("Insertion sort results:\n",list)
#testData.sort()
#if testData == list:
#print("Insertion sort was successful. No errors found.")
#return True
#else:
#print("Insetion sort failed. Review the arrays for errors. \n","Python sort \n",testData)
#return False




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

        elif y[j] < y[i]:
            x[k] = y[j]
            j = j+1

        else:
            x[k] = y[i]
            i = i+1


####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')

##################################### Enter Prams Here #######################################
n = 3 #Use n to create a random array of n**2 in size
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

####################################### Function Calls #######################################
mergeSort(a,[],0,len(a)-1)
print("Merge sort results: \n",a)

#mergeSort(b,[],0,len(b)-1,s)      #Expected crash
#print("Merge sort results: \n",b)

mergeSort(c,[],0,len(c)-1)
print("Merge sort results: \n",c)

mergeSort(d,[],0,len(d)-1)
print("Merge sort results: \n",d)

mergeSort(e,[],0,len(e)-1)
print("Merge sort results: \n",e)

mergeSort(f,[],0,len(f)-1)
print("Merge sort results: \n", f)

mergeSort(g,[],0,len(g)-1)
print("Merge sort results: \n",g)

mergeSort(h,[],0,len(h)-1)
print("Merge sort results: \n",h)

mergeSort(i,[],0,len(i)-1)
print("Merge sort results: \n",i)

mergeSort(j,[],0,len(j)-1)
print("Merge sort results: \n",j)

########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")
