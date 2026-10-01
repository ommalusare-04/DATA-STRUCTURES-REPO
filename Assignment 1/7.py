n = int(input("Enter the number of array elements you want: "))

li = []

for i in range(n):
    elements = int(input("Enter the array element: "))
    li.append(elements)

print(li)

position = 0

for i in range(n):
    if li[i] != 0:
        li[position] = li[i]
        position += 1

while position < n:
    li[position] = 0
    position += 1

print(li)