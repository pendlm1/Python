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

def binarySearch (x,y,m,c,cl,l):
    start = process_time()
    y.sort()
    try:
        
        if x[c] > y[len(y)-1]:
            binarySearch (x,y,m,c+1,cl,l)

        elif x[c] < y[0]:
            binarySearch (x,y,m,c+1,cl,l)

        elif x[c] > y[m]:
            cl = y[m+1:len(y)]
            m = int(len(cl)/2)
            binarySearch (x,cl,m,c,cl,l)

        elif x[c] < y[m]:
            cl= y[0:m]
            m= int(len(cl)/2)
            binarySearch (x,cl,m,c,cl,l)

        elif x[c] == y[m]:
            print(y[m], x[c])
            binarySearch (x,y,m,c+1,cl,l)
        end = process_time()
        print('\n Linear Search | Start:',start, ",", 'End:',end,'| Linear Search completed in:',end-start) 
    except IndexError:
        pass
    finally:
        pass
        
        
                

####################################### Timer Start ##########################################
start = process_time()
print('\n###############################################################################')
##################################### Enter Parms Here #######################################

path = "input_100.txt"
n = 5

####################################### Function Calls #######################################
myList = load(path)
testData = sampleList(n)
linearSearch(myList,testData)
binarySearch (myList,testData,int(len(testData)/2),0,[],[])
########################################## Timer End #########################################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")

