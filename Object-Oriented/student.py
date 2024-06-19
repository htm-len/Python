class Student:  # Represents a student with name and house attributes.
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing student name")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self.name = name  # Initialize student name
    self.house = house  # Initialize student house

def main():  # Creates a Student object and prints its information.
  student = get_student()  # Get student info (Student object)
  print(f"{student.name} from {student.house}")

def get_student():  # Prompts the user for student's name and house, returns a Student object.
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)  # Create a Student object

if __name__ == "__main__":
  main()

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
