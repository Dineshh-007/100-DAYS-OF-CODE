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

car = Car(make = "Nissan",model= "GT-R")
print(car.make)
