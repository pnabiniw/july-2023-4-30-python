student = {"name": "Hary", "age": 30, "department": "CS", "id": 3}

try:
    key = input("Enter the key you want to access ")
    data = student[key]
except KeyError:
    print("Please enter a key present in the dictionary")
else:
    print(f"The {key} of the student is {data}")
