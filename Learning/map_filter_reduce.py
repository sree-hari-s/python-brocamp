from functools import reduce


fruit=['apple','banana','pear','apricot']
test_map=map(lambda s:s[0]=='a',fruit)
print(list(test_map))

test_filter=filter(lambda s:s[0]=='a',fruit)
print(list(test_filter))

list=[2,4,7,3]
print(reduce(lambda x,y:x+y,list))