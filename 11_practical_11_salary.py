class emp:
    salary = 200
    increment = 1.75

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment =  sai/self.salary

e = emp()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 400
print(e.increment)
print(e.salary)
print(e.salaryAfterIncrement)
