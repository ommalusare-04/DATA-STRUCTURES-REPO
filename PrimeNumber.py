n=int(input("enter the number:"))
flag=0
for i in range(2,n//2+1):
    if n % i == 0:
        flag=1
        break
if flag==1:
    print("not a prime number:")
else:
    print("prime number")
    
    