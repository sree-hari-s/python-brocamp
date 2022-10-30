limit=int(input("Enter size of array:"))
array=list()
print("Enter array Elements:")
for i in range(limit):
    elements=int(input())
    array.append(elements)
print("Array:")
print(array)
print("Even numbers in the given array:")
for i in array:
    if i%2==0:
        print(i)