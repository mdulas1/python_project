from pickle import TRUE


n = 2//4
print(n)
class Calculator:
    def addition(self,num1,num2):
        return num1 + num2
    
    def subtraction(self,num1,num2):
        return num1 - num2
    
    
    def multiplication(self,num1,num2):

        return num1*num2
        
    def division(self,num1,num2):
        return num1/num2 if num2 != 0 else "can not be divide by zero"

test = Calculator()

num1 = int(input("enter num1\n>>>"))
num2 = int(input("enter num2 \n>>>"))

opretion = input("enter sign of operation\n>>>")
if opretion == "+":
    print(test.addition(num1,num2))
elif opretion == "-":
    print(test.subtraction(num1,num2))
elif opretion == "*":
    print(test.multiplication(num1,num2))
elif opretion =="/":
    print(test.division(num1,num2))
else:
    print("invalid option") 
