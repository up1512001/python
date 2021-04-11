class Employee:
    company = 'Utsav.org'

    def __init__(self,name,salary,unit):
        # super().__init__()
        self.name = name
        self.salary = salary
        self.unit = unit
        print("Employee created")

    def getSalary(self):
        print(f"Working in {self.company}")

    def detail(self):
        print(f"Name of employee is {self.name} and salary is {self.salary}K and working on {self.unit} unit")

    # def greating(self):
    #     print("Good Morning Form Utsav")

    @staticmethod
    def greating():
        print("Good morning from utsav")

    @staticmethod
    def time():
        print('!0 pm at night')


ut = Employee('utsav',200,'mobile')
# ut = Employee() this will throw error
# ut.getSalary()  # Employee.getSalary(ut)
# ut.greating()  # Employee.greating()
# ut.time()
ut.detail()



