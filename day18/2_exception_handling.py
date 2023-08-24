# Exceptions in Python can be handled using try...except block

try:
    num = int(input("Enter a number "))
except:
    print("Something Went Wrong")


# We can specify the error type in the except statement to catch the specific type of error
try:
    num = int(input("Enter a number "))
except ValueError:
    print("Please enter a valid number")


# We can catch multiple exception using the same except block
try:
    num = int(input("Enter a number "))
except (ValueError, KeyError, TypeError):
    print("Please enter a valid number and perform your operation properly")

try:
    num = int(input("Enter a number "))
except ValueError:
    print("Please enter a valid number")
except TypeError:
    print("Please check your operation")


# try...except...else...finally block
# else block is executed when no error occurs in the try block
# finally block is always executed no matter there is an error or not

try:
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
except Exception as e:
    print(e)
    print("please enter a valid number")
else:
    add = num1 + num2
    sub = num1 - num2
    prod = num1 * num2
    print(add)
    print(sub)
finally:
    print("This block is always executed !!")



