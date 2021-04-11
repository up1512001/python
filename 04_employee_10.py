
class Employee:
    comapny = 'Utsav.org'
    salary = 100
ut = Employee()
uts = Employee()

ut.salary = 300
uts.salary = 400

print(ut.comapny)
print(uts.comapny)
Employee.comapny = 'Utsav Patel.org'
print(ut.comapny)
print(uts.comapny)

print(ut.salary)
print(uts.salary)

# print(ut.salary)
# print(uts.salary)
