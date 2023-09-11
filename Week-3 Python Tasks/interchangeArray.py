limit=int(input("Enter limit of array:"))
array1=list()
print("Enter elements of array1:")
for i in range(limit):
    elements=int(input())
    array1.append(elements)
print("Enter elements of array2:")
array2=list()
for i in range(limit):
    elements=int(input())
    array2.append(elements)
print("Arrays before Swapping")
print(array1)
print(array2)
# for i in range(limit):
#     temp=array1[i]
#     array1[i]=array2[i]
#     array2[i]=temp
print("Array after Swapping:")
for i in range(limit):
    array1[i],array2[i]=array2[i],array1[i]
print(array1)
print(array2)