def year_of_birth(name,age):
    year = 2023-age
    print(f"Hello {name} you were born in {year}")

# create  a function that acccept any number in keyword(just like dictionary has key and values)
def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
