def decorate_me(func):
    def inner_fxn(*args, **kwargs):
        print("I am the extra functionality !!")
        return func(*args, **kwargs)
    return inner_fxn


@decorate_me
def message(txt1):
    return txt1


# message = decorate_me(message)
print(message("Hello World"))


@decorate_me
def message2(txt1, txt2, txt3="default"):
    return txt1 + txt2 + txt3


print(message2("Hello", "World", txt3="Im learning"))
