import random

randNumber = random.randint(1,100)
# print(randNumber)
userguess=None
guesses=0
while (userguess != randNumber):

    userguess = int(input('Enter Your Guess: '))
    if (userguess == randNumber):
        print('You Guess Right...')
    else:
        if userguess > randNumber:
            print('enter smaller Number..')
        else:
            print('enter larger number..')
        # print('Wrong Guess')
    guesses += 1

print(f'Total Guesses are {guesses}')

with open('hisscore.txt','r') as f:
    hs=int(f.read())
if guesses < hs:
    print('You set new Record...')
    with open('hisscore.txt','w')as f:
        f.write(str(guesses))


