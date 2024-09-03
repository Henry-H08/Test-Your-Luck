import random
import time
balance = 1000

wager = float(input(f'How much would you like to wager? Current Balance: {balance} '))
choices = [1, 2, 3, 4, 5, 6]

while True:
   
    start = input("Spin? Y/N. W to change wager")
    
    if start == "W":
         wager = float(input(f'How much would you like to wager? Current Balance: {balance} '))

    if start == "Y" and wager <= balance:
        thing1 = random.choice(choices)
        thing2 = random.choice(choices)
        thing3 = random.choice(choices)
    time.sleep(1)
    print("|===|")
    print(f'|{thing1}{thing2}{thing3}|')
    print("|===|")
    time.sleep(1)
    if thing1 == thing2 and thing1 == thing3:
        print("You Win")
        print("Current balance is: " + balance)
        winamount = wager * thing1
        balance = balance + winamount
    else:
        balance = balance - wager
 