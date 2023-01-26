class A:
    def __init__(self) :
        print("A class")

    def fun1(self):
        print("A fun1")


class B:
    def __init__(self):
        print("B class")

    def fun1(self):
        print("B fun1")


class C(B,A):
    def __init__(self):
        print("C class")

c = C()
c.fun1()
