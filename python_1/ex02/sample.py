#!/usr/bin/python3


class Sample:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


ob1 = Sample("Code-")
ob2 = Sample("Speedy")

ob3 = ob2 + ob2
print(ob3)


class Data_1:
    def __radd__(self, other):
        return 'Data 1:Called reverse +'


class Data_2:
    def __radd__(self, other):
        return 'Data 2:Called reverse +'


x = Data_1()
y = Data_2()

print("x + y", x + y)
print("y + x", y + x)
