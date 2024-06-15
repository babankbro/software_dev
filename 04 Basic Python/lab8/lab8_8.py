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

class Employee(Person):
    def __init__(self, name, age, email, salary):
        self.salary = salary
        Person.__init__(self, name, age, email)
        
    def update_salary(self, salary):
        self.salary = salary
        print(f"{self.name}'s salary has been updated to: {self.salary}")
    
    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}$")
           
    

employee1 = Employee("Jane Doe", 28, "janedoe@example.com", 50000)
employee1.display_info()
employee1.update_email("jane.doe@newdomain.com")
employee1.update_salary(55000)
employee1.display_info()