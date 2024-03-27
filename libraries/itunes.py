#Packages and libaries
import requests  # requests https://pypi.org/project/requests/
import sys  # sys library https://pypi.org/project/SysArg/
import json  # json library https://docs.python.org/3/library/json.html

# Check if at least two arguments are provided (script name + at least one name part)
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python script.py <FirstName> [LastName]")
    sys.exit()

# Combine all parts of the name provided into a single search term, joining with spaces
search_term = " ".join(sys.argv[1:])

# Construct the request URL with the combined search term
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + search_term)

# Get the response JSON
o = response.json()

# Initialize an empty set to hold unique track names
unique_track_names = set()

# Iterate over the results, adding each track name to the set to ensure uniqueness
for result in o["results"]:
    unique_track_names.add(result["trackName"])

# Sort the unique track names if you want them in alphabetical order
sorted_unique_track_names = sorted(unique_track_names)

# Print each unique track name, numbered and with space between entries
for index, track in enumerate(sorted_unique_track_names, start=1):
    print(f"{index}. {track}\n")