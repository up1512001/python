

class Person:
    def __init__(self):
        print('Initialization Person....')
    country = 'India'

    def takeBreadth(self):
        print('I am Breathing...')


class Employee (Person):
    def __init__(self):
        super().__init__()
        print('Initialization Employee....')
    company = 'Utsav.org'

    def getSalary(self):
        print(f'Salary is 100K')

    def takeBreadth(self):
        print('I am employee and breathing....')
        super().takeBreadth()

class programmer(Employee):
    def __init__(self):
        super().__init__()
        print('Initialization Programmer....')
    company = 'Patel'

    def takeBreadth(self):
        super().takeBreadth()
        print('I am programmer and breathing....')

    def getSalary(self):
        print(f'NO salary to programmer...')


p = Person()
e = Employee()
pr = programmer()

p.takeBreadth()
e.takeBreadth()
pr.takeBreadth()

print(e.company)
print(pr.company)

print(pr.country)



