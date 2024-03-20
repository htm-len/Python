#function iterating through loops
def main():
    number = get_number()
    meow(number)

def get_number():
    while True: 
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

# Call main to start the program
main()

#while loop 1
'''
i = 0
while i < 3:
    print("meow")
    i += 1
'''

#for loop - iterates over a list of items 
'''for i in range (3): 
    print(f"meow")'''

'''print("Meow\n" * 3, end="")'''

#while loop 2
'''while True: 
    n = int(input("What's n ? "))
    if n > 0:
      break

for _ in range(n):
   print("meow")'''
   