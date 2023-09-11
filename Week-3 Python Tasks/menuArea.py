class Area:
    def circle(self):
        r=int(input("Enter radius:"))
        area=float((22/7)*r*r)
        print("Area of Circle:",area)
    
    def square(self):
        a=int(input("Enter length of side:"))
        area=float(a*a)
        print("Area of Square:",area)
    
    def rectangle(self):
        l=int(input("Enter length of side:"))
        b=int(input("Enter breadth of side:"))
        area=float(l*b)
        print("Area of Rectangle:",area)
    
    def triangle(self):
        b=int(input("Enter base length:"))
        h=int(input("Enter height of triangle:"))
        area=float(l*b)
        print("Area of Triangle:",area)

class MyClass(Area):
    
    def Menu(self):
        
        while True:
            print("""Menu\n1.Area of Circle\n2.Area of Square\n3.Area of Rectangle\n4.Area of Triangle\n5.Exit\nEnter choice:""")
            choice = int(input())
            
            if choice == 1:
                self.circle()
            elif choice == 2:
                self.square()
            elif choice == 3:
                self.rectangle()
            elif choice == 4:
                self.triangle()
            elif choice == 5:
                break
            else:
                print("Enter valid input!")

m=MyClass()
m.Menu()
