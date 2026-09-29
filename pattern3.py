n=5
for i in range(0,n+1):
    for j in range(0,n):
        if j>=n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()