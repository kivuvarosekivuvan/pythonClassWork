#Write a Python program to find the largest number in a list.

def largest(nums):
    largest_num=max(nums)
    return largest_num

nums=[2,3,223,43656,6867]
largest(nums)


#Write a Python function that takes a list of numbers and returns a new list containing only the even
# numbers from the original list.
def evenList(lists):
    empty=[]
    for num in lists:
        if num %2==0:
            empty.append(num)
        return empty    
lists=[2,33,3,4,5,6,76,78]
evenList(lists)

#Reversing a string without using inbuilt
word="Rose"
reversing_word=""
for i in range (len(word)-1, -1, -1) #range generates sequences of the indices to iterate over
reversing_word +=word[i]             #-1:last index , -1:means we want to stop at the first character
print(reversing_word)                #-1:we want to step backward by 1 each time

#factorial numbers
if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#prime numbers
primes = []
for number in range(2, 101):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        primes.append(number)
print(primes)


#creating multiple list from a list
def many():
    lists= [[i for i in range(10)]for_in range(3)] #3 is number of times it creates
print    




