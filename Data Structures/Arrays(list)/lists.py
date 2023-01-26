x = [17,93,32,67,1,2,4,56,23]
#appending elements
x.append(100)
print(x)

#insert elements into list
# index where to add and values
x.insert(2,99)
print(x)


#remove elements

#remove specific numbers
x.remove(4)
print(x)

#remove specific index

x.remove(x[1])
print(x)

#slicing 
print(x[2::2])

x.sort()
print(x)

