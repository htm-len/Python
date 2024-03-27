import sys #Sys Module
# Import sys to access command-line arguments.

# Exit the program with a message if fewer than 2 arguments are provided (including the script name).
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Iterate over each argument provided (excluding the script name) and greet.
for arg in sys.argv[1: -1]:  # Skip the first argument (script name) for greeting.
    print("Hello, my name is:", arg)

'''
The commented-out section below offers an alternative approach 
where the script strictly expects exactly one additional argument 
and exits with a message if the arguments are too few or too many.

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("Hello, my name is:", sys.argv[1])
'''
