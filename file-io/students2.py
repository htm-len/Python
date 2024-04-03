# Import the CSV module
import csv  

# Prompt the user for name and home
name = input("What's your name? ")
home = input("Where's your home? ")

# Append the user-provided data to the CSV file
with open("students2.csv", "a") as file:  # Open the CSV file in append mode
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  # Create a CSV writer object
    writer.writerow({"name": name, "home": home})  
    # Write a new row containing the user's name and home
