n = 5
num=0
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(chr(65+num), end=" ")
        num+=1

    for j in range(i - 1, 0, -1):
        print(chr(65+num), end=" ")
        num+=1
    print()