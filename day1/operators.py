###### Operators #####
# Operators are the symbols in python or in any programming language that carry out arithmetic and logical
# operations
# The python operators are
# 1. Arithmetic Operators
# 2. Relational / Comparison Operators
# 3. Logical Operators
# 4. Membership Operators
# 5. Identity Operators
# 6. Assignment Operators


#### Arithemetic Operators ###
# 1. Addition (+)
a = 1
b = 2
print(a + b)
# Here a and b are operands whereas + is an arithmetic operator

# Subtraction (-)
a = 2
b = 1
print(a - b)

# Division
print(a / b)

# Multiplication
print(a * b)

# Modulus: Modulus operators gives remainder of the division operation
a = 4
b = 2
print(a % b)  # Result 0
print(5 % 2)  # Result 1

# Exponential (**)
print(a ** 2)  # 4**2 = 16
print(3**3)  # 27


# floor division (//)
# This operator omits the decimal values from the division operation and gives floor value
print(3 // 2)  # 1
print(-3 // 2)  # -2



######## Comparison Operators #########
# ==, <, >, >=, <=, != are the relational operators
# Relational operators give boolean result (True or False)

a = 5
b = 3
print(a == b)  # False
print(a > b)  # True
print(a < b)  # False
print(a != b)  # True



########## Logical Operators #############
# and, or, not are the logical operators
print(a > b or b != a)
print(a > b and a != b)
print(not True)  # False
print(not False)  # True

a = 5
print(not a)  # False
a = 0
print(not a)  # True. Here it is using the concept of truthy and falsy which we will learn later in this session



###### Assignment Operartors ##########
# is equals to (=) is the simplest assignment operator
a = 2 + 3
# In the above operation, 2 and 3 are added and assigned to a variable 'a' using assignment
# operator

a = 1
a = a + 1
print(a)  # 2
a += 1  # 3
# Here += is also an assignment operator
# Similarly -=, /=, *= all exist in similar manner
a = 20
a %= 2
print(a) # Gives 0


#### Membership Operators #####
# "in" and "not in" are the membership operators. We can use membership operator in sequence datatypes
print(2 in [1, 2, 3])  # True
print(3 not in [1, 2, 3])  # False


######### Identity Operators ################
# "is" and "is not" are the identity operators
a = [1, 2, 3]
b = a
print(a is b)  # True
# Here a and b are the same object and lies at same memory location
print(id(a) == id(b))  # True

b = a.copy()
print(a is b)  # False
print(id(a) == id(b))  # False
# Here a and b have same value but are in different memory location.\


##### Precedence and Associativity ######
# If an operation has multiple operators then precedence defines the order of such operators
# If multiple operators have same precedence then the operation is done based on associativity
# Normally all the operators have lef-right associativity except **

print(2 * 3 / 3)  # 2. Here multiplication and division have same precedence but the
# associativity is from left to right. So, multiplication is done first and then division

print(2 ** 3 ** 2)  # 512
# For ** associativity is from right-left. So, 3**2 is executed first and then 2 ** 9
