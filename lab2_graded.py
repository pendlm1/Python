# Lab 2 GRADED exercises
# Return only this script file

def fahr2celsius (f):
    return (f-32)*5/9
    
def shippingCost (d):
    if d>=0 and d<=50: 
        return d*5.00
    elif d>=51 and d<=200:
        return d*4.25
    elif d>=201 and d<=500:
        return d*3.95
    elif d>=501:
        return d*3.70
    
    
def  grader (avg_exams, avg_hw, attendance):
    if int(attendance) > 20 and float (avg_exams) > 70 and float(avg_hw) > 70:
        return True
    else:
        return False 


print ("The result of Fahrenheit to Celsius calculation",fahr2celsius(74))
print ("The result of shipping Cost calculation ",shippingCost(200))
print ("The result of course grader function ",grader(72,88,21))

        
        