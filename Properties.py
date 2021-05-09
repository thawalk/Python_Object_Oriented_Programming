# ---------- PROPERTIES (Python) -----------------

class SoftwareEngineer:

    def __init__(self):
        # one underscore is called a protected attribute , but still can be accessed from outside
        self._salary = None

    @property
    def salary(self):
        # check, constraints, calculations
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    
    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()

se.salary = 6000
print(se.salary)

# delete the attribute salary
# del se.salary
# print(se.salary)

# Recap:
# getter -> @property
# setter -> @x.setter


