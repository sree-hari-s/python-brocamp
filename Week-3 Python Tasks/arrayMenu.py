def getArray(n):
    print("Enter array elements:")
    array=list()
    for i in range(n):
        elements=int(input())
        array.append(elements)
    return array

def displayArray(ar):
    print("Array:",ar)
    
limit=int(input("Enter limit of array:"))
array1=getArray(limit)
displayArray(array1)