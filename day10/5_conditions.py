# Conditions are used for making decisions in a program
# There are four varieties of conditions we can creat
# 1. Simple if
# 2. if...else condition
# 3. if....elif...else ladder
# 4. nested if

# In the if conditions, the statement after the "if" is checked. If the statement is truthy then the
# condition is satisfied and the block inside the "if" is executed. Otherwise, it is not executed
a = 20
if a > 15:
    print("the number is greater than 15")

if a:
    print(f"The number is {a}")


# if...else
a = 20
if a > 15:
    print("the number is greater than 15")
else:
    print("the number is less than 15")

if a:
    print(f"The number is {a}")
else:
    print("The number is 0")


# if...elif...else ladder
exam_mark = 76
if exam_mark >= 80:
    print("Scored Distinction")
elif exam_mark >= 65:
    print("Scored First Division")
elif exam_mark >= 55:
    print("Scored Second Division")
elif exam_mark >= 40:
    print("Scored Third Division")
else:
    print("Failed")


# nested_if

a = 20
if a > 10:
    if a > 15:
        print(f"{a} is greater than 15")
    else:
        print(f"{a} is just greater than 10")
else:
    print(f"{a} is less than 10")



# ternary if
# One-liner conditions are called ternary if
a = 10
b = 5

if a > b:
    print("a is greater")
else:
    print("b is greater")

print("a is greater") if a > b else print("b is greater")  # One-liner ternary if


