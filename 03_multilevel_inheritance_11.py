
class Person:
    country = 'India'
    def takeBreadth(self):
        print('I am Breathing...')

class Employee (Person):
    company = 'Utsav.org'
    def getSalary(self):
        print(f'Salary is 100K')

    def takeBreadth(self):
        print('I am employee and breathing....')


class programmer(Employee):
    company = 'Patel'

    # def takeBreadth(self):
    #     print('I am programmer and breathing....')


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

