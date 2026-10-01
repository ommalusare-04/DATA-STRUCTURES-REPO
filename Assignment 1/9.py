s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special = 0

for i in s:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special Characters =", special)