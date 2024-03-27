# Try and except handling value error
try:
    x = int(input("What's x ? "))
except: 
    print("x is not an integer")
else:
    print(f"x is {x}")