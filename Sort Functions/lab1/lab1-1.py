#Mario Pendleton
#cs303
#lab1

from time import*
import random
import sys

def load (path):
    start = process_time()
    lst=[]
    file = open(path)
    strList = file.read().split()
    for i in strList:
        i = int(i)
        lst.append(i)
    file.close()
    end = process_time()
    lst.sort()
    print(lst)
    print('\n Loading Data | Start:',start, ",", 'End:',end,'| Data Loaded in:',end-start)
    return lst

def sampleList (n):
    start = process_time()
    sample = []
    k = 0
    for i in range(2**n):
        k = random.randint(0,2**n)
        sample.append(k)
    end = process_time()
    print('RD',sample)
    print('\n Random Data | Start:',start, ",", 'End:',end,'| Random data generated in:',end-start)
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
    return     
 
def binarySearch(k,y,l,r):
    start = process_time()
    m = 0
    if l > r:
        return True
    else:
        m = (r+l)//2
        
    if k > y[m]:
        print (k,">",y[m])
        return binarySearch(k,y,m+1,r)

    if k < y[m]:
        print (k,"<",y[m])
        return binarySearch(k,y,l,m-1)

    if k == y[m]:
        print("Search came back positive for",k)
    
    end = process_time()
    print('\n Binary Search | Start:',start, ",", 'End:',end,'| Binary Search completed in:',end-start)

        
                

####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')
##################################### Enter Parms Here #######################################

path = "input_100.txt"
n =94

####################################### Function Calls #######################################
myList = load(path)
print(myList)
binarySearch(n,myList,0,len(myList)-1)
########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")

