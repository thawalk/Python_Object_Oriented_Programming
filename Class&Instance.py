# ----------------- CLASS & INSTANCE -----------------

# primitive data structures such as lists and strings

# naive way of creating a object, not recommended.
# its cumbersome, should not be done this way
# position, name, age, level, salary
se1 = ["Software Engineer", "max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]



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

# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)

# print statement will throw error, because, name is a instance attribute
# print(SoftwareEngineer.name)

# both class and instance attribute
print(se1.alias)
print(SoftwareEngineer.alias)

