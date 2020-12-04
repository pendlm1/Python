################################################################################
# HW2, CS103 Fall 2018
# name:Mario Pendleton
# blazerid: B001158863
################################################################################
import math
################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'James Bond'
################################################################################

################################################################################
# helper function provided for your use in pixelLuminance: please do not change
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
################################################################################

##############
# HW2 PROBLEMS

##############
def p(x):                   # this is a practice problem that will not be graded
    if x<0 or x>1:
        return 0
    else:
        return 1

def isOdd (n):
    
   
    if type (n)!=int or n%2==0:
        return False
    elif type(n)==int:
        return True
    
  
        
def inAWhile (t, d): 
    assert type (t)==int
    assert type (d)==int
    h=t+d
    if h%12==0:
        return 12
    if h>12 or h <= -12:
        return h%12
    if h > -12 and h<1:
        return h//h
    else: 
        return h

def pixelLuminance (r, g, b):

    Er = 0.2126*r
    Eg = 0.7152*g
    Eb = 0.0722*b
    pix=int(Er+Eg+Eb)

    assert int(Er) and Er>=0 and Er<=255
    return pix


def iOverlap (a1, a2, b1, b2):
    #if a1>b1 and a1<b2 or a2>b1 or a1<b1 and a2>b1:
    if a1>=b1 and a1<=b2:
        return True
    elif a1<=b1 and a2>=b2:
        return True
    elif a1<=b1 and a2<=b2 and a2>=b1:
        return True
    elif a1>=b1 and a2>=b2 and a2>=b1:
        return True
    else:
        return False

def iOverlapLen (a1, a2, b1, b2):
    if a1>=b1 and a1<=b2:
        return b2-a1
    elif a1<=b1 and a2>=b2:
        return b2-b1
    elif a1<=b1 and a2<=b2 and a2>=b1:
        return a2-b1
    elif a1>=b1 and a2>=b2 and a2>=b1:
        return a2-a1
    else: 
        return False
    

def rOverlap (x1, y1, w1, h1, x2, y2, w2, h2):
    #Euclidean to find d(p,q) ~ hypo
    c = math.sqrt(((x2-x1)**2 + (y2-y1)**2)) 
    #Euclidea to find diff w and h
    b = math.sqrt(((w2-w1)**2 + (h2-h1)**2))
   
    return c<b
   
    

def rOverlapArea (x1, y1, w1, h1, x2, y2, w2, h2):
    
    #Euclidean to find d(p,q) ~ hypo
    c = math.sqrt(((x2-x1)**2 + (y2-y1)**2)) 
    #Euclidea to find diff w and h
    b = math.sqrt(((w2-w1)**2 + (h2-h1)**2))
    rArea1 = abs(h1)*abs(w1)
    rArea2 = abs(w2)*abs(h2)
        
    return (rArea2-rArea1)/(c-b)
    
def Hurray(n):
    a = 1
    result =""
    for i in range(n):
        if i == a:
            result = result + "hurray"
            a = a*2
        else:
            result = result + str(i)
    return result
            


print(Hurry(5))
   


