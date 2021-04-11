class animal:
    animalTyper = 'Mammal'

class pet (animal):
    color = 'white'

class dog (pet):
    @staticmethod
    def bark():
        print('Bow Bow...')

d = dog()
d.bark()
print(d.animalTyper)
print(d.color)