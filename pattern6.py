n = 5

for i in range(1, n+1):
    for j in range(1, n * 2):
        if j <= n - i or j >= n + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()