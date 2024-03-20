# Composing a list of dictionaries, where each dictionary contains information about a student.
# Each student has a name, the house they belong to in Hogwarts, and their patronus. 
# If a student does not have a patronus, it is marked as None.

students = [
    {
        "name": "Hermione",    # Student's name
        "house": "Gryffindor", # House in Hogwarts
        "patronus": "Otter"    # Magical creature conjured as a protective measure
    }, 
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russel Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None  # Represents the absence of a Patronus
    }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

'''
#Python Dictionary 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
'''


'''
# List is set of numbers and values 

#Iterate over the indices of the 'students' list using 'range(len(students))'
for i in range(len(students)):
    # Print the index (i) incremented by 1 to start numbering from 1 instead of 0, and the student name at that index
    print(i + 1, students[i])

#List 

students = ["Hermione", "Harry", "Ron"]

#For loops to iterate through the list starting starting with the 0 index
for student in students:
    print(student)
'''
