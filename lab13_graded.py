# -*- coding: utf-8 -*-
#la13_103fa18
#Mario Pendleton
#B001158863
import re

def func1(x,n):
    """Write a python function named as func1 that will take two integer values 
    as parameters, x and n, and will print from which function is running along
    with the message in below and return the x^n"""
    
    print("func1 is running: "+str(x)+"^"+str(n),"=",x**n)
    print("func1 is running: "+str(n)+"^"+str(x),"=",n**x)
    return
def func2(a,b):
    '''Write another function named as func2 that will again take two integer 
    values as parameters, a and b, and will print from which function is running 
    and the ab + ba value in the format below. Make sure that in your solution, 
    in func2 scope you call the func1.'''
    func1(a,b)
    print("func2 is running: "+str(a**b)+"+"+str(b**a),"=",a**b+b**a)
    return
def passValidate(password):
    '''Write a function “passValidate” that takes a string “s” and checks the 
    validity of string as a password Validation Rules:
• At least 1 lowercase letter between [a-z] and 1 upper case letter between 
  [A-Z].
• At least 1 number between [0-9].
• At least 1 character from [$#@].
• Minimum length 6 characters.
• Maximum length 16 characters.'''
    while True:
        if re.search("[a-z]",password):
            True
        else:
            return "Password must contain at least 1 lowercase letter [a-z]"
        if re.search("[A-Z]",password):
            True
        else:
            return "Password must contain at least 1 Uppercase letter [A-Z]"
        if re.search("[0-9]",password):
            True
        else:
            return "Password must contain at least 1 number [0-9]"
        if re.search("[$@#]",password):
            True
        else:
            return "Password must contain at least 1 of 3 characters [$#@]"
        if len(password)<6 or len(password)>16:
            return "Password must be between 6 and 16 characters long"
        return True

def luckySevens(l):
    '''Write a function called luckySevens which takes a list “l” which consists
    of integers and returns true if any three consecutive elements sum to 7.'''
    x,y,z = 0,0,0
    l2,l3 = 1,2
    try:       
        for i in l:
            x = i
            y =l[0+l2]
            z = l[0+l3]
            l2 += 1
            l3 += 1
            if x+y+z == 7: 
                return True
    except IndexError:
        return False
        
###############################################################################
######                      Change Varibles Below                        ######
###############################################################################

a = 2
b = 3
print("\n================================================================")
print("Results of func1 & func2: ")
func2(a,b) 

# Sample Input 1:
# func2(1,3)
# Sample Output 1:
# func1 is running: 1 ^ 3 = 1 
#func1 is running: 3 ^ 1 = 3 
#func2 is running: 1 + 3 = 4

print("\n================================================================")
print("Results of passValidate: ")
password="Uab@2762"
#At least 1 lowercase letter between [a-z] and 1 uppercase letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.'''
print(passValidate(password)) 

print("\n================================================================")
print("Results of luckySevens: ")
l = [2,3,4,1,2,4,0,2,7]
print(luckySevens(l))