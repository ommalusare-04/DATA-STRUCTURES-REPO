# n = int(input("Enter the number of array elements: "))
# arr = []

# for i in range(n):
#     val = int(input("Enter the array element: "))
#     arr.append(val)

# min = arr[0]
# max = arr[0]

# for i in range(n):
#     if arr[i] < min:
#         min = arr[i]

#     if arr[i] > max:
#         max = arr[i]

# print("Array:", end=" ")
# for i in range(n):
#     print(arr[i], end=" ")

# print()
# print("Minimum:", min)
# print("Maximum:", max)



# basic code

arr=[1,2,3,4,5,6,7]
min=arr[0]
max=arr[0]
for num in arr:
    if num<min:
        min=num
    if num>max:
        max=num
print(f"array elements are: {arr}")
print(f"max value is {max}")
print(f"min value is {min}")
