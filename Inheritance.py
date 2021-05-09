# ------------ INHERITANCE --------------

# base class 
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

# inherits from Employee
class SoftwareEngineer(Employee):
    # overriding __init__from base class
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    # overriding base class method by using the same method name
    def work(self):
        print(f"{self.name} is coding...")
    
    # extending upon the base class methods, by creating own methods unique to this class
    def debug(self):
        print(f"{self.name} is debugging...")


# inherits from Employee
class Designer(Employee):
    # extending upon the base class methods, by creating own methods unique to this class
    def draw(self):
        print(f"{self.name} is drawing...")

    # overriding base class method by using the same method name
    def work(self):
        print(f"{self.name} is designing...")

# this will throw error, need to pass in name and age as arguments
# se = SoftwareEngineer()

# creating a instance of SoftwareEngineer and Designer
se = SoftwareEngineer("Max", 25, 6000, "Junior")
print(se.name, se.age)
se.work()
print(se.level)
se.debug()

d = Designer("Philip", 27, 7000)
print(d.name, d.age)
d.work()
d.draw()


# ----------------- POLYMORPHISM -----------------

# subclasses can keep their own methods

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
            SoftwareEngineer("Lisa", 30, 9000, "Senior"),
            Designer("Philip", 27, 7000)]

print("------------ Polymorphism -------------")
def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

# Recap:
# inheritance: ChildClass(BaseClass)
#  inherit, extend, override
#  super().__init__()
#  polymorphism