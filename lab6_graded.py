# Lab 6 GRADED exercises
# Return only this script file
#Mario Pendleton
#B001158863

import random

def iSquare(n):
    i = 1
    while i<n:
        print(i**2)
        i=i+1     
    
def sConcatenate():
    x=""
    y=""
    while x != "done":
        x=str(input("Enter a word: "))
        y=y+" "+x
    print("Here is what you entered:",y[:-4])        

def guessNumber():
    chance = random.randint(1,100)
    x=0
    y=1
    print("I drew a number between 1 and 100. Can you guess what it is?")
    while x != chance:
        x=int(input("Enter what you think the number is? "))
        if x == chance:
            print('Nice!',chance,'is correct. You solved it in',y,'tries.')
        elif x > chance:
            print("You are too high. Try again")
        elif x < chance:
            print ("You are too low. Try again.")
        y=y+1
  
  



#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
n = 5
print ("The result of iSquare")
iSquare(n)
print ("\n**************************************")
print ("The result of sConcatenate ")
sConcatenate()
print ("\n**************************************")
print ("The result of guessNumber ")
guessNumber()
print ("\n**************************************")
