#UNLIMITED POSITIONAL ARGUMENTS

# def add(*args):
#     sum = 0
#     for n in args:
#         sum+=n
#     return sum
#
# print(add(5,6,7,8))

#kwargs ---> Keyword arguments
# def calculate(n,**kwargs):
#     print(kwargs)
#     n += kwargs["add"]  #do like dictionary
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2,add = 5 , multiply = 3)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        print(self.model)

car = Car(make = "Nissan",model= "GT-R")
print(car.make)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(toast='nah', spam=4, eggs=2)    # output:  4 2 nah 0


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)