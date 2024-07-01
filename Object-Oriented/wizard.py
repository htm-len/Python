class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing wizard name") 
        self.name = name

class Student(Wizard): 
    def __init__(self, name, house):  
        super().__init__(name)
        self.house = house  
            

class Professor(Wizard): 
    def __init__(self, name, subject):  
        super().__init__(name)
        self.subject = subject



wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Dumbledore", "Transfiguration")
print(student.name, student.house)  # Print the name and house of the student