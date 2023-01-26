#custom exception
try:
    raise Exception("you are ded")
except Exception as error:
    print(error)
else:
    print("you are alive")
finally:
    print("reborn again")
    

print("---------------------------------------")
#custom exception using class
class dogNotFound(Exception):
    print("inside class")

try:
    raise dogNotFound()
except dogNotFound:
    print("Dog not found ")
finally:
    print("Dog found finally")