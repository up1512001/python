
class Employee:
    company = 'Utsav.org.in'
    salary = 200
    location = 'damnagar'

    # def changeSal(self,sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSal(cls,sal):
        cls.salary = sal

e = Employee()
# salary is class attribute
print(e.salary)
print(Employee.salary)
e.changeSal(3000)
print(Employee.salary)
print(e.salary)

