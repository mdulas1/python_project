
p = 10000
r = 0.08
n = 12
t= float(input("enter the number of years :"))
A = p *(1 + r / n) ** (n*r)
print(f"the final amount after {t} years is {A:2f}")

