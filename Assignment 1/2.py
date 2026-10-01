n=int(input("entert thenumber of array elements you want:"))
sum=0
li=[]
for i in range(1,n+1):
    elements=int(input("enter the array element:"))
    sum+=elements
    li.append(elements)
min=min(li)
max=max(li)
print(f"minimum value is {min}")
print(f"maximum value is {max}")
