# Order of the function arguments is important to note
# Arguments are the values passed during function call and parameters are the
# values taken in function definition

# Order of the arguments
# 1. Positional / Compulsory Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments

def addition(a, b, c=10):  # here 'a' and 'b' are the positional arguments
    return a + b + c


print(addition(2, 3, c=5))  # 10  # here c is a keyword argument

# If we send value in the function call then the default value always gets override
# here c=5 overrides c=10



# Arbitrary Arguments
# Arbitrary arguments can take random number of elements in the function call. They are like an
# expandable bucket

def addition(*args):
    print(args)
    print(type(args))
    return sum(args)


print(addition(1, 2))  # 3
print(addition(1, 2, 3))  # 6
print(addition(1, 2, 3, 4, 5))  # 15


def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())


print(addition(a=1, b=2, c=3))  # 6
print(addition(a=1, b=2, c=3, d=4, e=5))  # 15

# Arbitrary arguments also have their own order. *args should always come before than **kwargs

def addition(a, b, c, d=1, e=2, f=3, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
    return a + b + c + d + e + f + sum(args) + sum(kwargs.values())


print(addition(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, p=14, q=15))


