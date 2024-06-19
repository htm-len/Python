class Student:  # Represents a student with name and house attributes.
    def __init__(self, name, house):
        self.name = name  # Initialize student name
        self.house = house  # Initialize student house

    def __str__(self):  # Returns a string representation of the student.
        return f"{self.name} from {self.house}"
  
    @property
    def name(self):  # Returns the student's name.
        return self._name
    
    @name.setter
    def name(self, name):  # Sets the student's name.
        if not name:
            raise ValueError("Missing student name")
        self._name = name

    @property
    def house(self):  # Returns the student's house.
        return self._house
    
    @house.setter 
    def house(self, house):  # Sets the student's house.:
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():  # Creates a Student object and prints its information.
    student = get_student()  # Get student info (Student object)
    student._house = "Number Four, Privet Drive"
    print(student)

def get_student():  # Prompts the user for student's name and house, returns a Student object.
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # Create a Student object

if __name__ == "__main__":
    main()



'''
    def __str__(self):  # Returns a string representation of the student.
        return f"{self.name} from {self.house}"

    def charm(self):  # Returns a visual representation of the student's patronus.
        magic = self.patronus
        if magic == "Stag":
            return "🦌"
        elif magic == "Otter":
            return "🦦"
        elif magic == "Jack Russell Terrier":
            return "🐕"
        else:
            return "🪄"'''

# def main():
#     """Gets student information (name and house) and prints it."""
#     student = get_student()  # Get student info (list)
#
#     # Check if student name is "Padma"
#     if student[0] == "Padma":
#         # Attempt to modify list element (not allowed because tuples are immutable)
#         student[1] = "Ravenclaw"  # This line will cause an error
#
#     print(f"{student[0]} from {student[1]}")
#
# def get_student():
#     """Prompts the user for student's name and house,
#        returns a list containing them (not a tuple)."""
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]  # Create a list
#
# if __name__ == "__main__":
#     main()
