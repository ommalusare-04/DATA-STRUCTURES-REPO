s = input("Enter the sentence: ")

li = s.split()

longest = li[0]
shortest = li[0]

for i in li:
    if len(i) > len(longest):
        longest = i

    if len(i) < len(shortest):
        shortest = i

print("Longest word:", longest)
print("Shortest word:", shortest)