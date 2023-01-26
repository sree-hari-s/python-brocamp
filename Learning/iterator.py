num=[1,2,3,4,5]
print(num.index(5)) #to find index of an element

for i in num:
    print(i)

print("-------------------")
it=iter(num)
print(it) #object of iteration

print("-------------------")
#method 1
print(it.__next__())
print(it.__next__())
print("-------------------")
#method 2
print(next(it))