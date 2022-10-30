number=int(input("Enter limit: "))
sum=0
for i in range(1,number+1,2):
    if i%2!=0:
        sum+=i
print("Sum of odd numbers till",number,"is:",sum)