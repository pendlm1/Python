# Lab 7 GRADED exercises
# Return only this script file

def argMin(l1):
    n = 0
    k = l1[0]
    for i in l1:
        if i<k:
            n=i
    return n
       
def grList(l2):
    MyList = l2[:]
    BudsList = []
    for i in l2:
        if i == "peanut" or i == str("carrot"):
            i = "apple"
            BudsList.append(i)
    print(BudsList)
        
            
    
    return #ADD CODE HERE    

def gcDivisor(k,m):
    return #ADD CODE HERE  
    



#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
l1 = [ 44,33,24,66,1,123,65]
print ("The result of argMin")
print(argMin(l1))
print ("\n**************************************")
l2 = ["water", "chips", "watermelon", "peanut", "napkins"]
print ("The result of grList ")
grList(l2)
print ("\n**************************************")
k = 54
m = 81
print ("The result of gcDivisor ")
gcDivisor(k,m)
print ("\n**************************************")
