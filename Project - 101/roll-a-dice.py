import random

response = "y"

while response == "y":
    no = random.randint(1, 6)

    if no == 1:
        print("[-----]")
        print("[ ]")
        print("[ ⚽ ]")
        print("[ ]")
        print("[-----]")

    if no == 2:
        print("[-----]")
        print("[⚽  ]")
        print("[   ]")
        print("[   ⚽ ]")
        print("[-----]")

    if no == 3:
        print("[-----]")
        print("[ ]")
        print("[⚽⚽⚽]")
        print("[ ]")
        print("[-----]")

    if no == 4:
        print("[-----]")
        print("[⚽⚽]")
        print("[ ]")
        print("[⚽⚽]")
        print("[-----]")

    if no == 5:
        print("[-----]")
        print("[⚽ ⚽]")
        print("[ ⚽ ]")
        print("[⚽ ⚽]")
        print("[-----]")

    if no == 6:
        print("[-----]")
        print("[⚽⚽⚽]")
        print("[ ]")
        print("[⚽⚽⚽]")
        print("[-----]")

    response = input("press y to roll again and n to exit")
    print("\n")                        
