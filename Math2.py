################################################################################
# HW1, CS103 Fall 2018
# name: Mario Pendleton
# blazerid: B01158863
################################################################################

import math      # you will need the math module to answer some of the questions
from typing import Tuple
Pt2 = Tuple(float,float)
################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Mario Pendleton'
################################################################################

##############
# HW1 PROBLEMS
##############

def f(x):                   # this is a practice problem that will not be graded
    # ADD CODE HERE
    return 5*x - 3

def areaCircle (r):
    # ADD CODE HERE
    return math.pi * r**2

def nSnookerBall (nRow):
    # ADD CODE HERE
    return nRow*(nRow+1)//2

def eApproximately (n): 
    # ADD CODE HERE
    return (1+(1/n))**n

def volCone (r, h):
    # ADD CODE HERE
    return 1/3 * math.pi * r**2 * h

def distOrigin (x, y):
    # ADD CODE HERE
    return math.sqrt(x**2+y**2)

def dist2(p: Pt2, q: Pt2) -> float
    return

def lengthSegment (x1, y1, z1, x2, y2, z2):
    # ADD CODE HERE
    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

def getInRange(x,a,b):
    assert a == float(a)
    assert b == float(b)
    assert x == float(x)
    if a < b:
        if a < x and b > x:
            return x
        elif a > x:
            return a
        elif b < x:
            return b
    else:
        if a > x and b < x:
            return x
        elif a < x:
            return a
        elif b > x:
            return b

