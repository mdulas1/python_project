ages = [33,25,18,15,33,17]
for age in ages:
    if age <=17:
        ages.remove(age)
        print("remove under 18 age")
    else:
        print("person",age)

ages.sort()
print("ages list",ages)