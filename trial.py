db={"a":2,"b":4,"c":5}

i=input("Enter the input:")
for j in db:
    if i==j:
        print("found")
    else:
        print("Not found")