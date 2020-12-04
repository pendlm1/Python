# Lab 8 GRADED exercises
# Return only this script file

def sumOfEven(n):
    if n==0:
        return 0
    return n+(sumOfEven(n-2)) 
    
def triangleChecker():
    tri = open('triangle.rtf','r')
    tri.readline()
    tri.readline()
    tri.readline()
    tri.readline()
    tri.readline()
    tri.readline()
    tri.readline()
    side1 = tri.readline()
    side1=int(side1[14:-2])
    side2 = tri.readline()
    side2=int(side2[:-2])
    side3 = tri.readline()
    side3=int(side3[:-1])
    if side1==0 or side2==0 or side3==0:
        print("The triangle is invalid")
    elif side1==side2 and side2==side3:
        print("Valid triangle: Equilateral")
    elif side1!=side2 and side2!=side3 and side3!=side1:
        print("Valid triangle: Scalene")
    else:
        print("Valid triangle: isosceles")
     
    



#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
n=10
print ("The result of sumOfEven")
print(sumOfEven(n))
print ("\n**************************************")
print ("The result of triangleChecker")
triangleChecker()
print ("\n**************************************")
