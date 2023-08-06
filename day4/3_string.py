# Strings are the immutable datatypes in Python
# They are sequential datatypes (iterables)

# Creating an empty string
a = ""
b = ''
c = """
"""   # docstring / triple-quoted string
d = '''
'''   # docstring / triple quoted string
e = str()   # str() is a built-in function


# Quote Characters
message = "I'm learning Python"  # double quote outside and single quote inside
# message = 'I'm learning Python'   # This raises error

message = 'He said, "Python is awesome!"'  # single quote outside and double quote inside
# message = "He said, "Python is Awesome !""  # This raises error

# But we have the feature of escape sequence in python if we want to use single quote both inside
# and outside

message = 'I\'m learning Python'  # here \' is an escape sequence
message = "He said, \"Python is awesome!\""  # here \" is an escape sequence


# Escape sequence suppresses the usual meaning of character and gives new meaning
# \', \", \n, \t etc are escape sequences

print("Hello\nWorld")  # "Hello" <newline> "World
print("Hello\tWorld")  # Hello <tab> World



############### Triple Quoted Strings #################

# Triple quoted strings can be used as docstring. We can write docs for function and classes using
# triple-quoted strings. Sometimes they are also used as multiline comments.
# They can be stored in a variable like regular strings


def addition(a, b):
    """
    This is a function to add two integers
    :param a: First integer input
    :param b: Second integer input
    :return: sum of a and b
    """
    return a + b


print(help(addition))

message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque 
condimentum lectus nibh, eu molestie nulla vestibulum a. 
In venenatis turpis vel turpis dignissim maximus. 
Donec scelerisque ligula sit amet nunc tempor semper. 
Sed semper arcu ligula, sed tempor felis fringilla vehicula. 
Sed sit amet dapibus nisi. Curabitur tempor ipsum vel erat dictum, 
at laoreet ipsum dictum. Phasellus id turpis vel neque porta lacinia eu nec nibh. 
Vestibulum ut nulla in erat ultrices congue quis at purus. 
Vestibulum dignissim quam ac eros interdum convallis. 
"""
