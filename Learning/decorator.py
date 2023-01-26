def decorator_func(func):
    def wrapper_func():
        print("wrapper func worked")
        return func()
    print("Decorator worked")
    return wrapper_func

def show():
    print("show worked")
    
decorator_show=decorator_func(show)
print("----------------")
decorator_show()

print("----------------")
#alternate method
@decorator_func
def display():
    print("display worked")
display()