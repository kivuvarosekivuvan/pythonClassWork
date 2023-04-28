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
    
       















