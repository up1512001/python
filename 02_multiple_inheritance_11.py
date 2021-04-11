

class Employee:
    company = 'Utsav.org'
    ecode = 200

class freeLancer:
    company = 'patel'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer (Employee, freeLancer):
    name = 'uts.patel'


p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)

