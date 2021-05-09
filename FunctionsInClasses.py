# ----------------- Functions In Classes -----------------

# primitive data structures such as lists and strings

# naive way of creating a object, not recommended.
# its cumbersome, should not be done this way
# position, name, age, level, salary
se1 = ["Software Engineer", "max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]



# example as to why functions should be inside classes
d1 = ["Designer", "Philip"]
def code(se):
    print(f"{se[1]} is writing code...")
code(d1)


# class is a blueprint on how a object/instance should be defined

# class
class SoftwareEngineer:

    # class attribute, tied to the class itself and the instance that is created
    alias = "Keyboard Magician"

    # initializer/ constructor, runs when the instance is first defined
    def __init__(self, name, age, level, salary):
        # instance attributes, only tied to the instance that is created
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    # instance method with parameter
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # instance method to return some data
    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    # special methods
    
    # this method is executed whenever the object is converted to a string
    # dunder method
    def __str__(self):
        salary = f"salary = {self.salary}"
        return salary

    # method to override default default equals methos which compares memotry addr of instances
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # this is a method that can be invoked from the class and not the instance
    # def entry_salary(age):
    #     if age < 25:
    #         return 5000
    #     if age < 30:
    #         return 7000
    #     return 9000

    # this is the proper way of defining it, so both class and instance can invoke it, but cannot access any instance attributes withing this method
    # such as self.name, self.age, it will throw error
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

# creating instances
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
se3 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se1.name, se1.age)

# print statement will throw error, because, name is a instance attribute
# print(SoftwareEngineer.name)

# both class and instance attribute
print(se1.alias)
print(SoftwareEngineer.alias)

# calling the instance method
se1.code()

# calling instance method with parameter
se1.code_in_language("Python")
se2.code_in_language("C++")

# calling instance method that returns data
print(se1.information())

# invoking special method whenever the object is converted to a string
print(se1)

# invoking equals method
print(se2 == se3)

# below will throw error
# se1.entry_salary(24)

# invoking a static method
print(SoftwareEngineer.entry_salary(27))
print(se1.entry_salary(24))


# recap:
# instance method(self)
# can take arguments and can return values
# special "dunder" method (__str__ and __eq__)
# @staticmethod