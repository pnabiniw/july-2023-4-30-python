# Decorators are the functions that add extra functionality to the existing function


def decorate_me(func):
    def inner_fxn():
        print("I am the extra functionality !!")
        return func()
    return inner_fxn


@decorate_me
def message():
    print("Hello World")


# message = decorate_me(message)
message()





