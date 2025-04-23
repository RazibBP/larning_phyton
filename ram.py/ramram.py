import random
playing = True
while playing:
    chose = input("Roll the dise? y/n : ")

    if chose == 'y':
        dise1 = random.randint(1,6)
        dise2 = random.randint(1,6)
        print(f"({dise1}, {dise2})")
    elif chose == 'n':
        print("Thnaks for playinG:")
        break
    else:
        print("Inviled Choise.")
