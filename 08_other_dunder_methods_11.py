class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print('lets multiply')
        return self.num * num2.num

    def __str__(self):
        return f'Decimal Number:{self.num}'

    def __len__(self):
        return 1

    
n1 = Number(23)
n2 = Number(15)
print(n1)
print(len(n1))
