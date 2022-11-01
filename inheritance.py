class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
            
    def function1(self):
        print("this is a parent")
    
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,age)
        self.lastname="hari"
        self.age=39
    
    def display(self):
        print(self.name,self.age) 
        
    def function2(self):
        print("This is child  class")
        
child1=Child("sree",22)
child1.display()