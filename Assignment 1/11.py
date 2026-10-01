s = input("Enter the sentence: ")
li = s.split()
for i in li:
    print(i[::-1], end=" ")
