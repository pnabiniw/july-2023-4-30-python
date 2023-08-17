data = "All the occurrences of a specified character in a given string"
picked_char = input("Pick a character ")
result = ""
for each in data:
    if each.lower() == picked_char.lower():
        continue
    result += each

print(result)
