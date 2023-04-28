def add(a,b):
    answer= a+b
    return answer

def sum(*numbers):
    answer=0
    for number in numbers:
        answer += number
    return answer    

def subtract(z,y):
    answer2= z-y
    return answer2

def divide(m,n):
    answer3= m/n
    return answer3

def multiply(p,r):
    answer4= p*r  
    return answer4  

def remainder(w,q):
    answer5= w%q
    return answer5    

def sum(*numbers):
    answer=0
    for number in numbers:
        answer += number
    return answer

# create a function that can accept any number of intergers and return the result of multiply all of them
def multi(*nums):
    answer=1
    for num in nums:
        answer*=num
    return answer











