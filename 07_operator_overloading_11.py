class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self,num2):
        print('lets multiply')
        return self.num * num2.num

n1 = Number(23)
n2 = Number(15)
sum =n1 + n2
mul = n1*n2
print(sum,mul)
