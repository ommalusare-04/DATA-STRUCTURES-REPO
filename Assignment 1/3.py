n=int(input("enter the number of array elements you want:"))
oddcount=0
evencount=0
for i in range(n):
    if i % 2 == 0:
        evencount+=1
    
    else:
        oddcount+=1

print(f"even count is {evencount}")
print(f"odd count is {oddcount}")