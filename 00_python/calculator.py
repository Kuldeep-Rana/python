class Calculator:

    current_val = 0 


    def add(self, number):
        self.current_val += number
        print(self.current_val)

    def minus(self, number):
        self.current_val -= number
        print(self.current_val)

    def multiply(self, number):
        self.current_val *= number
        print(self.current_val)

    def devide(self, number):
        self.current_val /= number
        print(self.current_val)



obj =  Calculator()

obj.add(10)
obj.add(20)


obj.minus(15)    
obj.minus(5) 

obj.multiply(3)
obj.multiply(2) 

obj.devide(4)
