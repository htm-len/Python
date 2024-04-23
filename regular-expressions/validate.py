import re  # Import the regex module

# Prompt for user's email and remove extra spaces
email = input("What's your email? ").strip()

# Validate the email format using regex
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    # This regex matches a typical .edu email address
    print("Valid")   # Print "Valid" if email matches the pattern
else:
    print("Invalid")  # Print "Invalid" if it does not match
