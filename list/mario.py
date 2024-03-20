#Time Stamp 4:00:00
def main():
    print_square(3)

def print_square(size):
    # Iterate through each row in the square
    for i in range(size):
        # Iterate through each "brick" in the row
        for j in range(size):
            # Print a brick without newline, stay in the same row
            print("#", end="")
        # After completing a row, print a newline to start a new row
        print()

main()
