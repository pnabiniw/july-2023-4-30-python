# We do string formatting using f-string

programming_language = input("Enter a language ")
message = f"I am learning {programming_language}"
print(message)


name = "John Doe"
age = 23
message = f"Hello I am {name}. I am {age} years old"

print('I am %s and I am %d years old' % (name, age))
print('I am {}'.format(name))
