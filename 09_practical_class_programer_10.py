class Programmer:
    company = 'MicroSoft'
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'company name is {self.company} name of programmer is {self.name} and working product is {self.product}')

ut = Programmer('utsav','365 office')
ut.getInfo()