n=7
for i in range(1,n+1):
    for j in range(1,n*2):
        if j>=i and j<=n*2-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()