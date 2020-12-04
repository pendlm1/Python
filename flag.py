# -*- coding: utf-8 -*-
################################################################################
# HW6, CS103 Fall 2018 Johnstone
# name: Mario M. Pendleton
# blazerid: B01158863
################################################################################


from turtle import*
import random
from math import*
'''You will use randomization to vary how you draw your flags. The bottom left 
corner of the first flag is drawn at a random point in the rectilinear square 
bounded by (-200,-200) and (0,0). Each flag is of the same width w, which is 
chosen randomly in (100,200). The gap between consecutive flags should be a 
random number between 1 and 10. Since these random numbers determine the size 
and position of the flags, each time you run the code you should see a slightly 
different drawing. The use of random size and position is my way of encouraging 
the use of variables over magic numbers. A statement like ‘forward(40)’ uses a
magic number 40. A statement like ‘forward(w/2)’ where ‘w’ has a semantic 
meaning of width, is much better: it documents your thought, and it is easily 
generalized to different widths.'''

# if you prefer, you may replace this import with:
# from turtle import *
# which will allow you to use left rather than turtle.left

# please add other functions to help you divide and conquer this problem
# (thought exercise: what basic units of code do you reuse several times?)
# (thought exercise: what basic units of code have a clean semantic meaning?)

def randomsizes(x,y,w,s):
    '''
    Params:
        x (Random int bewteen(-200 & 0): X value of cartesian coordinate system
        y (Random int between(-200 & 0): Y value of cartesian coordinate system
        w (Random int between(100 & 220): Distance traveld by pixel from a to b
        s (Random int between(1 & 10): Distance between objects.
    Returns: maritime signal flags MMP Mike Mike PAPA ~

    '''
    y,x = random.randint(-200,0),random.randint(-200,0)
    w = random.randint(100,200)
    s = random.randint(1,10)
    return (x,y,w,s)

def flagInitials (x,y,w,s):
    begin_fill()
    speed(5)
    setheading(0)
    up()
    goto(x,y)
    down()
    for i in range(3):       
        for i in range(4):
            fd(w)
            rt(90)
        up()
        fd(w+s)
        down()
    up()
    
def firstInitial(x,y,w,s):
    goto(x,y)
    color("white","blue")
    end_fill()
    begin_fill()
    color("white","white")
    for i in range(2):
        fd(w*.15)
        rt(45)
        fd(abs(sqrt((w*.85)**2+(w*.85)**2)))
        up()
        rt(45)
        fd(w*.15)
        rt(90)
    end_fill()
    fd(w)
    setheading(180)
    begin_fill()
    for i in range(2):
        fd(w*.15)
        lt(45)
        fd(abs(sqrt((w*.85)**2+(w*.85)**2)))
        lt(45)
        fd(w*.15)
        lt(90)
    end_fill()
    setheading(0)
    fd(s) 
    
def middleInitial(x,y,w,s):
    color("white","blue")
    end_fill()
    begin_fill()
    color("white","white")
    for i in range(2):
        fd(w*.15)
        rt(45)
        fd(abs(sqrt((w*.85)**2+(w*.85)**2)))
        up()
        rt(45)
        fd(w*.15)
        rt(90)
    end_fill()
    fd(w)
    setheading(180)
    begin_fill()
    for i in range(2):
        fd(w*.15)
        lt(45)
        fd(abs(sqrt((w*.85)**2+(w*.85)**2)))
        lt(45)
        fd(w*.15)
        lt(90)
    end_fill()
    setheading(0) 
    fd(s+w/3)
    rt(90)
    fd(w/3)
    
def lastInitial(x,y,w,s):
    setheading(0)
    begin_fill()
    for i in range(4):
        fd(w/3)
        rt(90)
    end_fill()
    done()
    
y,x = random.randint(-200,0),random.randint(-200,0)
w = random.randint(100,200)
s = random.randint(1,10)

print("\n=================================================================")
print(randomsizes(0,0,0,0))
flagInitials (x,y,w,s)
firstInitial(x,y,w,s)
middleInitial(x,y,w,s)
lastInitial(x,y,w,s)