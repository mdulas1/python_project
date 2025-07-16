# A simple calculator app
print('''********************
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. exponential
************************
      Enter two numbers to add
      ''')
first_number =  input("first number:")

second_number =  input("second number:")
sum = float( first_number) + float(second_number)
print(f"{first_number} + {second_number}: = {sum}")

print("***************")
print("subtraction")
print("enter two number to subtract")

first_number =  input("first number:")

second_number =  input("second number:")
sub = float( first_number) - float(second_number)
print(f"{first_number} - {second_number}: = {sub}")

print("***********************")
print("multiplication")
print("enter two number to multiply")
first_number =  input("first number:")

second_number =  input("second number:")
mul = float( first_number) * float(second_number)
print(f"{first_number} + {second_number}: = {mul}")

print("**********************")
print("division")
print("enter two number to divide")
first_number =  input("first number:")

second_number =  input("second number:")
div = float( first_number) // float(second_number)
print(f"{first_number} + {second_number}: = {div}")

print("***********************")
print("exponential")
print("enter base and power")

first_number =  input("first number:")

second_number =  input("second number:")
exponent = float( first_number) ** float(second_number)
print(f"{first_number} ^ {second_number}: = {exponent}")


