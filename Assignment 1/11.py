str = input("Enter the string: ")
li = [str]
print()
print(str)
for i in range(len(li)):
    print(li[i][::-1])
