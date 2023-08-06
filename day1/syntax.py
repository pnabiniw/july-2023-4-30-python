#####Identifier#####
# Any name of a variable, function or class provided by the user is an identifier

# Rules of naming identifiers in python
# 1. Identifiers are case-sensitive i.e. Area and area are two different variables
# 2. Identifiers can't be python keywords.
# 3. Identifiers name can have A-Z, a-z, 0-9 and _
# 4. But it can't start with digit. 1a = "hello". Here 1a is invalid identifier.
# 5. We can't use special symbols like @, $, # as identifiers.


### Python Statement ####
# Each line in a python code is a statement
# We can separate multiple statements in same line using semicolon ;
# We can also use back-slash \, for the line continuation

message = "Hello World"
message1 = "Hello"; message2 = "World"
message = "Hello " \
          "World"
import csv, \
    json

# Indentation in python is very important to represent a code-block
# Let's see an if code block in C language

# if(a==1){
# printf("Hello World")
#
# }
a = 1
b = 2
if a == 1:
    print("Hello World")
    if b == 2:
        print("2 is also printed")
    print("This is outside b")
print("This is not in if code block")
