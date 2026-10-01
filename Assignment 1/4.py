n = int(input("Enter the number of array elements: "))
li = []
for i in range(n):
    element = int(input("Enter the array element: "))
    li.append(element)

print(li)
search = int(input("Enter the number to search: "))
position = 0
for i in range(1,n+1):
    if li[i] == search:
        position = i
        print(f"{search} present in array at position {position+1}")
        break
    else:
        print(f"{search} not present in array")




