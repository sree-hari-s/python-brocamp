class Student:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s=Student()
print(s.sum())
print(s.sum(1))
print(s.sum(1,2))
print(s.sum(1,2,3))