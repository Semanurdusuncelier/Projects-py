from itertools import count
import random
from re import L

number = random.randint(0,50)

luck=random.randint(0,50)
luck=5 

while luck > 0 :
    luck-=1
    count +=1
    guess = int (input("guess :"))
    if number == guess:
        print (f"Congrate {count} .you're find !! , Total score : {100-(20)*5 (count)}")
        break
    elif number> guess :
        print("Number is hıgh")
    else :
        print("Number is low")
    if guess == 0:
        print("Ahh you're luckless ")