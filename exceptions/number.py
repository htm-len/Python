def main():
    # Get an integer from the user and print it.
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # Return the user's input as an integer.
            return int(input(prompt))
        except ValueError:
            # If input isn't an integer, retry.
            pass

main()
