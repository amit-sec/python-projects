import random
#written during code with harry session

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you =='g':
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
randNo = random.randint(1, 3)

if randNo == 1 :
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("Your's Turn :  Snake (s) water (w) or Gun (g) ?")
a = gameWin(comp, you)

print(f"comp chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("You win")
else:
    print("You loose")