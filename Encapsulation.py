# ----------- ENCAPSULATION AND ABSTRACTION -----------------

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private attributes

        # double underscore is called a private attribute, cannot be accessed from outside
        # self.__salary = 5000

        # one underscore is called a protected attribute , but still can be accessed from outside
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1
    
    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        # check value, enforce constraints
        # example:
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        self._salary = self._calculate_salary(base_value)
    
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se = SoftwareEngineer("Max", 25)

print(se.name, se.age)
print(se._num_bugs_solved)

# this will throw error
# print(se.__salary)

for i in range(70):
    se.code()



se.set_salary(6000)
print(se.get_salary())

# Recap:
# encapsulation 
# abstraction 
# public, private
# _foo(), _x 
# getter/setter
