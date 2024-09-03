thing1 = 0
thing2 = 0
thing3 = 0

import random
import time

choices = [1, 2, 3, 4, 5, 6]
while True:
    print("|===|")
    print(f'|{thing1}{thing2}{thing3}|')
    print("|===|")
    time.sleep(1)
    start = input("Spin? Y/N ")

    if start == "Y":
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