import random

# rock paper seasor and snack water gun both are same

def game(comp,you):
    if comp == you:
        return None
    elif comp =='s':
        if you =='w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# print("Computer  turn : Snack(s) Water(w) Gun(g)?")
comp = ''
randNo = random.randint(1,3)
if randNo==1:
    comp = 's'
elif randNo==2:
    comp ='w'
else:
    comp = 'g'
you = input("Your turn : Snack(s) Water(w) Gun(g)?")
li = ['s','w','g']
if you not in li:
    print("Enter Valid...")
else:
    x = game(comp,you)

    if x == None:
        print("Game Is Tie")
    elif x:
        print("You Win...")
    else:
        print("You Loss !!!") 


