# classes
class Employee:  # name of the class

    empCount = 0

    def __init__(self, name, salary):  # class constructor
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):  # further methods are defined like functions
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary : ", self.salary)


# Create first object of employee class

emp1 = Employee("Ben", 2000)

emp2 = Employee("Edi", 3000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)