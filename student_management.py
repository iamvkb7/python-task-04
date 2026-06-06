class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


student = Student("vimal", 101, 88)
student.display()
