
class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)
    
    def __str__(self):
        if self.imaginary <0:
            return f'{self.real} - {-self.imaginary}i'
        return f'{self.real} + {self.imaginary}i'

    def __mul__(self,c):
        mulreal = self.real*c.real - self.imaginary*c.imaginary
        mulimg = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulreal,mulimg)



c1 = Complex(-1,3)
c2 = Complex(-4,6)
print(c1+c2)
print(c1*c2)