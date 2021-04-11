
class Employee:
    #  class attributes
    comapny = 'Utsav.org'
    salary = 100
    

# during assignment and reading instance variable first get found
# and if not found then it will go to class defination
ut = Employee()
uts = Employee()
# creating instance attributes
ut.salary = 300
uts.salary = 400

uts.salary = 200
print(ut.salary)
print(uts.salary)

# print(ut.salary)
# print(uts.salary)
