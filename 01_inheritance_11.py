# single inheritance
class Employee:
    company = 'Utsav.org'

    def showdefain(self):
        print('this is employ class')

class programmer (Employee):
    name = 'python'
    # company = 'patel.org'
    def getName(self):
        print(f'language is {self.name}')

    def showdefain(self):
        print('this is programmer class')

e = Employee()
p = programmer()
e.showdefain()
p.getName()
p.showdefain()
print(p.company)