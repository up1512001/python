import random

def game():
    ran = random.randint(1,1000)
    return ran


score = game()

with open('high.txt') as f:
    hig = (f.read())

if hig == '':
    with open('high.txt','w')as f:
        f.write(str(score))       
elif int(hig) < score:
    with open('high.txt','w')as f:
        f.write(str(score))



