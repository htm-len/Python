class Student:  # Represents a student with name and house attributes.
    def __init__(self, name, house):
        self.name = name  # Initialize student name
        self.house = house  # Initialize student house

    def __str__(self):  # Returns a string representation of the student.
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)  # Create a Student object

def main():  # Creates a Student object and prints its information.
    student = Student.get()  # Get student info (Student object)
    print(student)


if __name__ == "__main__":
    main()
