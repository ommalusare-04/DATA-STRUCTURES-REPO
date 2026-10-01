n=int(input("entert thenumber of array elements you want:"))
sum=0
li=[]
for i in range(1,n+1):
    elements=int(input("enter the array element:"))
    sum+=elements
    li.append(elements)

new_li=[]
for i in li:
    if i not in new_li:
        new_li.append(i)

print(f"original array:{li}")
print(f"after removing duplicates:{new_li}")

