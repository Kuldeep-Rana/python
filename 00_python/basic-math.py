class BasicMath:

        
    def add(self, a,  b):
        return a+b

    def minus(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a / b

opr =  BasicMath ()

sum = opr.add(10,20)
print("sum is "+str(sum))

minus = opr.minus(100,20)
print("minus is "+str(minus))

multi = opr.multiply(10,2)
print("multiply is "+str(multi))

divide = opr.divide(100,20)
print("divide is "+str(divide))