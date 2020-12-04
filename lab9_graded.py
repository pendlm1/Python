# Lab 9 UNGRADED exercises
# These exercises are for practice only
# Mario Pendleton
# B01158863

from turtle import*    
import math

def flSquare(n,s):
    speed(0)
    shape("turtle")
    goto(0,0)
    setheading(0)
    for i in range(4):
        fd(n)
        lt(90)
    pu()
    setx(n+s+s)
    pd()

def frSquare(n,s):
    setheading(90)
    for i in range(4):
        fd(n)
        rt(90)
    pu()
    sety(n+s+s)
    pd()
    
def goSquare(n,s):
    begin_fill()
    goto(n+s+s,n+s+n+s)
    goto(n+s+s+n,n+s+n+s)
    goto(n+s+s+n,n+s+s)
    goto(n+s+s,n+s+s)
    end_fill()
    pu()
    setx(n/2+s/2)
    sety(n+s+(s/2))
    pd()
    
def nrSquare(n):
    setheading(45)
    for i in range(4):
        fd(n/4*3)
        lt(90)
    pu()
    goto(-s,200)
    pd()

def flTriangle(n,s):
    setheading(180)
    color("red","red")
    for i in range(3):
        fd(n)
        lt(120)
        
def goTriangle(n,s):
    pu()
    goto(-s,0)
    pd()
    begin_fill()
    goto(-n-s,0)
    goto(-n/2-s,math.sin(90)*n)
    goto(-s,0)
    end_fill()
    pu()
    goto(-n-2*s,0)
    pd()
    
def frTriangle(n,s):
    setheading(0)
    for i in range(3):
        rt(-120)
        fd(n)
    done()
 
#############################################################################
#               !!! You Can Change the parameters !!!

print ("\n======================================")
n=80
s=n/4
#############################################################################

print ("Results of flSquare")
flSquare(n,s)
print ("\n======================================")

print ("Results of frSquare")
frSquare(n,s)
print ("\n======================================")

print ("Results of goSquare")
goSquare(n,s)
print ("\n======================================")

print ("Results of nrSquare")
nrSquare(n)
print ("\n======================================")

print ("Results of flTriangle")
flTriangle(n,s)
print ("\n======================================")

print ("Results of rtTriangle")
goTriangle(n,s)
print ("\n======================================")

print ("Results of goTriangle")
frTriangle(n,s)
print ("\n======================================")
