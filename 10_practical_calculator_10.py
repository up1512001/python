class cal:
    def __init__(self,num):
        self.number = num

    def square(self):
        # pass
        print(f'value of {self.number} square is {self.number**2}')

    def squareRoot(self):
        # pass
        print(f'value of {self.number} root is {self.number**0.5}')

    def cube(self):
        # pass
        print(f'value of {self.number} cube is {self.number**3}')


a = cal(49)
a.square()
a.squareRoot()
a.cube()