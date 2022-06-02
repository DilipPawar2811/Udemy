#self keyword is mandatory for calling variables names into methods
#instance (dynamic) and class (static) variables have whole different purposes
#constructor name should be __init__

class Calculator:
    num = 100 # class variables
    def __init__(self,a, b):
        self.firstNumber= a
        self.secondNumber= b
        print("i am called automatically when object is created no need to create object and called")


    def getData(self):
        print("i am executing as method in class")

    def sumation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) #to create objects
print(obj.sumation())
obj.getData()

obj1 = Calculator(4, 5) #to create objects
print(obj1.sumation())
obj1.getData()


