################################################################################
# HW5, CS103 Fall 2018 Johnstone
# name:Mario Pendleton
# blazerid:B01158863
################################################################################

################################################################################
# will be used by the autograder
import math
def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Mario Pendleton'
################################################################################
# helper function: please do not change
import decimal
def significant (d, n):
    """Given a desired precision, express a float to this level of precision.
    >>> significant (12.345678, 4)
    12.35
    Params: 
        d (float): # of interest
        n (int):   precision (# significant digits)
    Returns: (float) d rounded to this precision
    """

    decimal.getcontext().prec = n
    return float(decimal.Decimal(d) / decimal.Decimal (1))
################################################################################

def longest (L):
    Lmax,K,L1="","",[]
    j,n,a,b,c = 0,0,105,110,103
    for i in L:
        K = list(i)
        j = len(i)
        if K[j-3]==chr(a) and K[j-2]==chr(b) and K[j-1]==chr(c) and j%2==0:
            L1.append(i)
            if j>n:
                Lmax=i
                n=n+j
    return Lmax
                
def argLongest (L):
    Lmax,K,L1="","",[]
    j,n,a,b,c = 0,0,105,110,103
    l2 = -1
    for i in L:
        K = list(i)
        j = len(i)
        if K[j-3]==chr(a) and K[j-2]==chr(b) and K[j-1]==chr(c) and j%2==0:
            L1.append(i)
            if j>n:
                Lmax=i
                n=n+j
                l2=L.index(Lmax)
    return l2
 
def eApprox (n):
    e1,e2,k = 0,1,1
    while significant(e1,n) != significant(e2,n):
        e1=(1+1/k)**k
        k += 1
        e2=(1+1/k)**k
    return e2

def hurray (n):
    c,s = 0,""
    for i in range(0,n+1):
        k = 2**c
        if i == k:
            i = "hurray"
            s=s+i
            c += 1
        else:
            s=s+str(i)
    return s


