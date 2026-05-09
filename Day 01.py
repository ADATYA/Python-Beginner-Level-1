#................
#Printing in Python
#................

# How to print "Hello World" in Python
print('Hello World')

# How to print multiple items in a single line
print("My favourite movie is", "Fast and Furious", "Wolf ot wall street", "The Dark Knight")

#......................
# Variables in Python
#......................

name = 'Bikrom Adatya Roy'
age = 24
cgpa = 3.30
print ("My name is .name, I am {age} years old and my cgpa is {cgpa}")
print ("My name is {}, I am {} years old and my cgpa is {}".format(name, age, cgpa))

# way2 : 
print(name)
print(age)
print(cgpa)
# ...............................
# Data Types in Python...
#................................
name = "Bikrom Adatya Roy" # String
phn_num = 1234567890 # Integer
cgpa = 3.30 # Float
is_student = True # Boolean

my_interger = 20
print('Integer:', my_interger) # Output: Integer: 20

my_float = 3.69
print("Float:", my_float) # Output: Float: 3.69

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>


#.......................
#isinstance function in Python
#........................

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False 

input = name = "Bikrom Adatya Roy"  # this is true
input num = 12345678901 # thats why this line are not executes but this line is also true.

if isinstance(name, str):
    print("This is a string!")
elif isinstance(num, int):
    print("This is a integer number")
else:
    print("This is differnt datatypes")



#.....................................................................
# Mini Poject 01 based on Data type / Variable / Function (isinstance)
#.....................................................................

# User input 
user_input = input("Enter anything :")
#Input is't integer?
if user_input.isdigit():   #isdigit = এই মেথডটি চেক করে স্ট্রিংয়ের ভেতরে শুধু সংখ্যা আছে কি না। যদি থাকে, তবেই আমরা সেটাকে int() দিয়ে সংখ্যায় রূপান্তর করতে পারি।
    print(f"This is a integer number:{num}")
# If doesn't integer then it's call string
else:
    name = user_input
    print(f"This is a string value:{name}")
    
#.....................................................................
# Mini Poject 02 based on Function calling methods
#.....................................................................

def check_data_type (data):
    if isinstance(data, bool):
        return "This is a Boolean value"
    elif isinstance(data , int):
        return "This is an Integer number"
    elif isinstance(data, str):
        return "This is a String"
    else:
        return "Unlock data type"

## How to show the Output
print(check_data_type(37))          # o/p = "This is an Integer number"
print(check_data_type("John Doe"))  # o/p =  "This is a String"
print(check_data_type(True))        # o/p =   "This is a Boolean value"
