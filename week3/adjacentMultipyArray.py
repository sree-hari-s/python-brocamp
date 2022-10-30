limit=int(input("Enter limit of array:"))
array=list()
print("Enter array elements:")
for i in range(limit):
    elements=int(input())
    array.append(elements)
newArray=list()
for i in range(limit-1):
    newArray.append(array[i]*array[i+1])
print("Original array:")
print(array)
print("New array after multiplying adjacent elements:")
print(newArray)