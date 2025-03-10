#Task 1: Students Class

#Defining Class
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def printStudentInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

#Initializing Objects of Class Students
Raj = Students("Raj", 16, "11th")
Joe = Students("Joe", 17, "11th")
#Printing info with methods built in
Raj.printStudentInfo()
Joe.printStudentInfo()

print("\n\n")
#Task 2: Parent Class Staff, Child Class Teacher

#Parent Class
class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
#Child Class inheriting from Parent
class Teacher(Staff):
    def __init__(self, name, department, role, salary, age):
        super().__init__(name, department, role, salary)
        self.age = age

    def printTeacherInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}")

#Initializing Objects
Raj_Teach = Teacher("Raj", "Science", "Teacher", 60000, 24)
Joe_Teach = Teacher("Joe", "Science", "Teacher", 72000, 58)
#Printing them with the methods built in
Raj_Teach.printTeacherInfo()
Joe_Teach.printTeacherInfo()



print("\n\n")



#Task 3: Python Class Square

class Square():
    def __init__(self, side):
        self.side = side
    def squarePerimeter(self):
        return self.side * 4
    def squareArea(self):
        return self.side ** 2

#Initializing objects
sq1 = Square(4)
sq2 = Square(16)

#Printing the area and perimeter
print(f"The Area of sq1 is {sq1.squareArea()}")
print(f"The Perimeter of sq1 is {sq1.squarePerimeter()}")
print(f"The Area of sq2 is {sq2.squareArea()}")
print(f"The Perimeter of sq2 is {sq2.squarePerimeter()}")