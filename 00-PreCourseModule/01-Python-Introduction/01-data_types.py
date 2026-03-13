# name = "Rahul" #string
age = 25  # integer
price = 19.99 # float
is_active = True #boolean 
middle_name =None # None is a special data type in Python that represents the absence of a value. It is often used to indicate that a variable has no value or that a function does not return anything.


#common string operations 

name = "  Rahul Mishra  "
print(name.lower()) # prints "  rahul mishra  "
print(name.upper()) # prints "  RAHUL MISHRA  "
print(name.strip()) # prints "Rahul Mishra"
    # prints "  Muskan Mishra  "
print(name.split()) # prints ['Rahul', 'Mishra']
print(name[0]) # prints "R"


email = "user@example.com"
print(email.startswith("user"))
print(email.endswith(".com"))

is_at = "@" in email 
print("@ is there" if is_at == True else "@ is not there")
