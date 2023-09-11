def addition(num1,num2):
    print("Sum is ",num1+num2) 
def subtraction(num1,num2):
    print("Difference is ", num1-num2)
def division(num1,num2):
    print("Division is ", num1/num2)
def multiplication(num1,num2):
    print("Multiplication is ", num1*num2)
    
choice=int(input("Menu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter choice: "))
x = float(input("Enter 1st number: "))
y = float(input("Enter 2nd number: "))
if choice==1:
    addition(x,y)
elif choice==2:
    subtraction(x,y)
elif choice==3:
    multiplication(x,y)
elif choice==4:
    division(x,y)
else:
    print("Invalid input")