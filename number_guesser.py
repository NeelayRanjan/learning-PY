import random
from time import sleep
guess=input("What number between 1-10 do you want to guess ")
int(guess)
answer=random.randint(1,10)
if answer==guess:
    print("You Won")
else:
    #print("You lost\n"+"The answer was: "+answer)
#sleep(5)
