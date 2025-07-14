age = int(input("ENTER YOUR AGE:"))
if age >18:
    if age < 60:
        print("adult")
    else:
        print("senoir")

else:
    if age >12:
        print("teenager")
    else:
        print("child")