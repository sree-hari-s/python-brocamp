def sum( list1 ):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    print(sum)


list1=[1,2,3,4,5]
sum(list1)