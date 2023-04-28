#Write and invoke one function that takes in a random string and returns the
#following values: first character, last character, length of the string and
#whether it begins with a vowel or not















#Create a function that takes in a password as a parameter. For a password to
#be valid it must meet the following conditions:
#1. Must be at least 8 characters long
#2. Must be at most 16 characters long
#3. Must not be “password”
#4. Must contain a digit
#Your function should determine whether the password provided is valid or not.
#The function returns true/false (7pts)
def is_valid_password(password):
    if len(password) < 8 or len(password) > 16:
        return False
    elif password == "password":
        return False
    elif not any(char.isdigit() for char in password):
        return False
    else:
        return True
