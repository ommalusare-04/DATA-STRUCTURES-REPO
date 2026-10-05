n=int(input("enter the number of rows:"))
num=0
for i in range(0,n+1):
    for j in range(i+1):
        print(chr(65+num),end=" ")
        num+=1
    print()