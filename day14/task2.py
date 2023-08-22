# Create a decorator "login_required" which checks the password provided by the user.
# If the password matches "1234" then the user can access the function else show message
# "Your password is invalid"

def login_required(func):
    def inner_fxn(*args, **kwargs):
        pw = input("Enter the password ")
        if pw == '1234':
            return func(*args, **kwargs)
        else:
            return "Your password is invalid"
    return inner_fxn


@login_required
def addition(a, b):
    return a + b

print(addition(2, 3))  # 5


