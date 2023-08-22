# Create a function that takes a text message and simply return the text message
# Create a decorator which changes the text message into the upper case text.

def to_upper_case(func):
    def inner_fxn(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) != str:
            return result
        return result.upper()
    return inner_fxn


@to_upper_case
def message(txt):
    return txt


print(message("hello world"))
