
class Employee:
    company = "Utsav.org"
    def getSalary(self):
        print(f"Salary is {self.sal}K in working company {self.company}")

ut = Employee()
# ut.getSalary()
# Employee.getSalary(ut)
ut.sal = 10000000
ut.getSalary() # Employee.getSalary(ut) both are same




