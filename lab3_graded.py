# Lab 3 GRADED exercises
# Return only this script file

def listInsert (l2,x):
    l2.append(x)
    l2.sort()
    l2.reverse()
    return l2
    
def tupleLast3 (t2):
    assert len(t2)>3  
    return t2[-3]  
    
    
def  str2tuple (s3,s4):
    return tuple(s3+s4)

#############################################
#   !!! DO NOT MODIFY THE CODE BELOW !!!
#############################################

l2 = [2, 5, 7, 8, 11]		
x = 6
print ("The result of listInsert ",listInsert (l2,x))
t2= ("u", "a", "b", "2", "3", "4", "c", "i", "s")
print ("The result of tupleLast3 ",tupleLast3 (t2))
s3 = 'Hello'
s4 = "World"
print ("The result of str2tuple ",str2tuple (s3,s4))     