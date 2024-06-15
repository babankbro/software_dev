class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
    
    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email has been updated to: {self.email}")

class Student(Person):
    def __init__(self, name, age, email, student_id):
        self.student_id = student_id
        self.courses = []
        Person.__init__(self, name, age, email)
        
    def enroll_course(self, subject):
        print(f"{self.name} has enrolled in {subject}.")
        self.courses.append(subject)
    
    def display_courses(self):
        msg = ''
        for subject in self.courses:
            msg += subject + ', '
        msg = msg.strip(", ")
        print(f"{self.name}'s Courses: {msg}.")
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        self.display_courses()
   
class Teacher(Person):
    def __init__(self, name, age, email, teacher_id):
        self.teacher_id = teacher_id
        self.course_teachings = []
        Person.__init__(self, name, age, email)
        
    def add_course(self, subject):
        print(f"{self.name} has enrolled in {subject}.")
        self.course_teachings.append(subject)
    
    def display_courses(self):
        msg = ''
        for subject in self.course_teachings:
            msg += subject + ', '
        msg = msg.strip(", ")
        print(f"{self.name}'s Teaching Courses: {msg}.")
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.teacher_id}")
        self.display_courses()
   

university = [
    Teacher("Dr. Smith", 45, "drsmith@university.com", "T001"),
    Teacher("Prof. Johnson", 50, "johnson@university.com", "T002"),
    Teacher("Ms. Davis", 38, "davis@university.com", "T003"),
    Student("Alice", 20, "alice@student.com", "S001"),
    Student("Bob", 22, "bob@student.com", "S002"),
    Student("Charlie", 19, "charlie@student.com", "S003"),
    Student("Mr.A", 20, "alice@student.com", "S004"),
    Student("Mr.B", 22, "bob@student.com", "S005"),
    Student("Mr.C", 19, "charlie@student.com", "S006")
]
# Demonstrating polymorphism
for i, person in enumerate(university):
    if isinstance(person,  Student):
        continue
    print(i+1, end=". ")
    person.display_info()
    print("----------")