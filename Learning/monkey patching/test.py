import monkey
def monkey_func(self):
    print("monkey function is called")
    
monkey.A.func=monkey_func
obj= monkey.A()

obj.func()