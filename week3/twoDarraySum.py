def getArray(limit):
    array=[]
    for i in range(limit):
        elements=[]
        for j in range(limit):
            elements.append(int(input()))
        array.append(elements)
    return array

limit=int(input("Enter limit of 2D array:"))
print("Enter 1st array elements:")
array1=getArray(limit)
print(array1)