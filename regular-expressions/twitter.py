import re 

# This script extracts a Twitter username from a provided URL.
url = input("URL: ").strip()  # Prompt the user for a URL and remove any leading or trailing whitespace.

# Use the walrus operator to perform a regex search and assign the result to 'matches'. 
# This combines the assignment and the condition check in one line.
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")  # Print the username if a match is found.
