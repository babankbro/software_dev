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
   


student1 = Student("Alex Smith", 20, "alexsmith@example.com", "S123456")
student1.display_info()
student1.enroll_course("Mathematics")
student1.enroll_course("Physics")
student1.enroll_course("Programming")
student1.display_courses()
student1.update_email("alex.smith@university.com")
print()
student1.display_info()
