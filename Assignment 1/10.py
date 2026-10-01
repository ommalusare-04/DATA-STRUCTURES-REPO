s = input("Enter a string: ")
sub = input("Enter substring: ")

count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        print("Found at position:", i)
        count += 1

print("Total occurrences:", count)
