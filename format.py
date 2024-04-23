import re  # Import the regular expression module

# Get the user's name and remove extra spaces
name = input("What's your name ? ").strip()

# Check if the name is in 'Last, First' format and rearrange if true
# The ':=' (walrus operator) is used here to perform assignment and condition check in one line
if matches := re.search(r"(^.+), *(.+)$", name):
    # If a match is found, reformat the name by swapping first and last names
    name = matches.group(2) + " " + matches.group(1)  # Reorder to 'First Last'

# Greet the user with the possibly modified name
print(f"Hello {name}")
