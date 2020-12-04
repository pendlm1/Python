# Lab 2 UNGRADED exercises
# These exercises are for practice only
import math

def bmiCalculator(wt,h):
    return (wt*703)/h**2
    

def f(X,Y):
    return int((X+Y)**3//math.sqrt(X**2+Y**2))



def passwordChecker(id_number,password):
    if id_number == 141520 and password == 135792468:
        return True
    else: 
        return False
    

print ("The result of BMI calculation",bmiCalculator(250,72))
print ("The result of f function ",f(5,4))
print ("The result of passwordChecker ",passwordChecker(141520,135792468))
