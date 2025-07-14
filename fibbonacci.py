def fibonacci(n):
    if 20 <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    # print the first 20 fibonacci number
num = input("enter the nth term")
print(num)
for i in range(20):
    print(fibonacci(num))
         