class Calculator:
    def add(self,a,b):
        return a + b
    
    def multiply(self,a,b):
        return a * b
    
    def divide(self,a,b):
        return a / b if b!=0 else "cannot divide by zero"
    
        
    def subtract(self,a,b):
        return a - b
    
calc = Calculator()
print(f" addition of two nu{calc.add(2,9)}")
print(calc.multiply(4,9))
print(calc.divide(7,2))
print(calc.subtract(10,7))
