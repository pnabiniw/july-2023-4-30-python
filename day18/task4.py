def is_vowel(char):
    if any([char.isnumeric(), len(char) > 1, type(char) != str]):
        return False
    return char.lower() in ["a", "e", "i", "o", "u"]


character = input("Enter a character")
result = is_vowel(character)
print(result)
