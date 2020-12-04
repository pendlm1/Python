# -*- coding: utf-8 -*-
# Lab 10 UNGRADED exercises
# Mario Pendleton

def dSquare(n):
    '''Write a function “dSquare” that takes an int “n” and returns a dictionary. 
    The keys of the dictionary are numbers between 1 to n (both included) and the  
    values are square of keys.'''
    d={}
    for i in range(1,n+1):
       d[i]=i**2
    return d
 
def dMerge (d1,d2):  
    '''Write a function “dMerge” that takes two dictionaries “d1” and “d2” and 
    returns another dictionary (combination of d1 and d2). The function is to 
    add values for common keys.'''
    d={}
    for i in d1:
        if i in d2:
            d1[i]=d1[i]+d2[i]
    d.update(d2)
    d.update(d1)
    return d  
      
def dShakespeare(m):
    '''Write a function “dShakespeare” that takes an int “m” and returns the
    how many times they occur in the Shakespeare play from FolgerDigital Texts.
    '''
    folger = open("a_midsummer_nights_dream_folger.txt","r")
    msnd = folger.read()
    d={}
    c=0
    j=0
    d1=""
    for char in "!@#$%^&*()_+;',./<>?:-=[]{}\|":
        msnd=msnd.replace(char,"")
    msnd=msnd.split()
    for i in msnd:
        c=msnd.count(i)
        d[i.lower().replace("'","")]=c
    return d
    

#############################################################################
    #              !!! Parameters can be changed below!!!               #
#############################################################################

print ("\n◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊")
n=5
print("The results of dSquare:")
print(dSquare(n))

print ("\n◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊")
d1 = {'a': 250, 'b': 100, 'c':600}
d2 = {'a': 150, 'b': 450, 'd':300}
print("The results of dMerge:")
print(dMerge(d1,d2))

print ("\n◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊")
m=10
print("The results of dShakespeare:")
print(dShakespeare(m))