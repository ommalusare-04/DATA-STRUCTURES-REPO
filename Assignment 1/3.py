n=int(input("entert thenumber of array elements you want:"))
sum=0
li=[]
oddcount=0
evencount=0
for i in range(1,n+1):
    elements=int(input("enter the array element:"))
    sum+=elements
    li.append(elements)

for i in li:
    if i % 2 == 0:
        evencount+=1
    else:
        oddcount+=1
print(f"all array elements are:{li}")
print(f"Even count is {evencount}")
print(f"Odd Count is {oddcount}")