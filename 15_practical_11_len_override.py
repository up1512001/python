
class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ''
        index = 0
        for i in (self.vec):
            str1 += f' {i} a{index} +'
            index += 1

        return str1[:-1]

    def __add__(self, v):
        newList = []
        if len(self.vec) != len(v.vec):
            print('Length of v1 and v2 must be same')
        else:
            for i in range(len(self.vec)):
                newList.append(self.vec[i]+v.vec[i])
            return vector(newList)

    def __mul__(self, v):
        sum = 0
        if len(self.vec) != len(v.vec):
            print('Length of v1 and v2 must be same')
        else:
            for i in range(len(self.vec)):
                sum += (self.vec[i]*v.vec[i])
            return sum

    def __len__(self):
        return len(self.vec)

v1 = vector([1, 3, 4, 4, 5, 9])
v2 = vector([2, 3, 4, 4, 2])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))
