import csv  # Import the CSV module

# Initialize an empty list to store student data
students = []

# Read student data from the CSV file
with open("students.csv") as file:
        reader = csv.DictReader(file)  # Create a CSV reader object
        for row in reader:  # Iterate over each row in the CSV file
            students.append(row)  # Append student data as a dictionary

# Sort students by name and print their details
for student in sorted(students, key=lambda student: student["name"]):  # Sort students by name
    print(f"{student['name']} is in {student['home']}")  # Print each student's name and home
