

import random
import time
balance = 1000

choices = [1, 2, 3, 4, 5, 6]
while True:
    wager = float(input("How much would you like to wager? Current Balance: " + balance))
    start = input("Spin? Y/N ")
    
    

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