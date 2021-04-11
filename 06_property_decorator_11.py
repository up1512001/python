class Employee:
    company = 'patel'
    salary = 3450
    salarybonus = 300
    # totalSalary = 3756

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val-self.salary



e = Employee()
print(e.totalSalary)
e.totalSalary = 4000
print(e.salarybonus)
print(e.salary)






    