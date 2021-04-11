class Employee:
    company = 'Utsav.org'
    def getSalary(self):
        print(f"Working in {self.company}")

    
    # def greating(self):
    #     print("Good Morning Form Utsav")
    @staticmethod
    def greating():
        print("Good morning from utsav")
    @staticmethod
    def time():
        print('!0 pm at night')

ut = Employee()
ut.getSalary() # Employee.getSalary(ut)
ut.greating() # Employee.greating()
ut.time()