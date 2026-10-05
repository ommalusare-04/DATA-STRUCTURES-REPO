n=int(input("enter the number of rows:"))
for i in range(0,n+1):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()