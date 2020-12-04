################################################################################
# HW4, CS103 Fall 2018 Johnstone
# name: Mario Pendleton
# blazerid: B001158863
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Mario Pendleton'
################################################################################

def eCount (s):
    n,j = 0,1
    for i in s:
        if i==chr(101) or i==chr(69):
            n=n+j
    return n

def consonantCount (s):
    s1=s.upper()
    n=0
    for i in s1:
        if i>=chr(66) and i<=chr(90):
            n=n+1
        if i==chr(69) or i==chr(89) or i==chr(73) or i==chr(79) or i==chr(85):
           n=n-1
    return n
        
def pigglyWiggly (w):
    x=w[0]
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="y":
        return w+"yay"
    else:
        return w[1:]+x+"ay"