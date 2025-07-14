# function to check if a number is even or odd
def check_number(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
# main function
def main():
    number = int(input("enter a number"))
    result = check_number(number)
    print(f"the number is {result}")

# program start here