students = []

# Read student data from the CSV file
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# Define a function to get the student's name for sorting
def get_house(student):
    return student["house"]

# Sort students by name and print their details
for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")




'''with open("students.csv") as file: 
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")'''