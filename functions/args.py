def my_country(country):
    print(f"Hello from {country}")

# A function named concatenate_args that takes any number of string arguments in positional arguments 
# format and concatenates them into a single string
def concatenate_args(*stringx, y="/" ):        
    return y.join(stringx)                      
    

# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments 
#  format and concatenates them into a single string
def concatenate_kwargs(**details):
    d=" "
    for key,value in details.items():
        d+=value
    return d

#Finding a factorial of a number
def factorial(num):
    if num ==0:
        return 1
    else:
        return num *factorial(num)   

num = 5
print(factorial(num))  

#Checking a string is palindrome
def palindrome(string):
    s=string.replace(" ", "").lower() #first remove all spaces and change to lowercase
    return s==string(::-1)  #checkingif string is same when reversed

string = "raceCar"
print(palindrome(string))    
  
    
       















