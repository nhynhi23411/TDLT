#Function has no arguments
def greet():
    print("Hello, world!")

greet()
#Function that takes arguments and returns no results
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Nhi")
#Function that takes arguments and returns results
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  
print(result) 

