num = int(input("enter the number:"))
p=len(str(num))
sum=0
n=num
while n != 0:
    sum+=(num%10)**p
    num=num//10

if sum==n:
    print("Armstrong number")
else:
    print("not a armstrong number")