class vec3:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'

v = vec3(2,3,4)
print(v)