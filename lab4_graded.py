# Lab 4 GRADED exercises
# Return only this script file

# Mario Pendleton
# B01158863

def letterCount (s1,s2):
    let=list(s2)
    sen=list(s1)
    for let in let:
        i=let,sen.count(let)
        print (i)

def fibonacci (n):
    j=0
    k=1
    for i in range(n):
        k, j=j, k+j
        print(k)
    
def  oddChecker (t):
    for i in t[:]:
        if i%2!=0:
            print(i)
  

#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
s1 = "do you want to go to the movies tonight"
s2="qwerty"
print ("The result of letterCount ")
letterCount (s1,s2)

print ("\n**************************************")
n=5
print ("The result of fibonacci ")
fibonacci (n)

print ("\n**************************************")
t = (1,2,3,5,8,22,35,92,123)
print ("The result of oddChecker ")
oddChecker (t)    
print ("\n**************************************")
