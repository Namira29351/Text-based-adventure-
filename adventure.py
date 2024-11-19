def start_game():
    print("Hello adventurer, you are in a fairytale forest! Choose your destiny wisley.\n")
    playerOneInput = input("Choose your Path: \n Path1: GO NORTH \n Path2: CLIMB OAK TREE....")
    if playerOneInput == "GO NORTH":
        print("Looks like you didn't choose wisely...")
        start_game()
    elif playerOneInput == "CLIMB OAK TREE":
        print("You found a map!! Go West")
        west()
    else:
        print("Something went wrong! Try Again!")

def west():
    print("You are now facing two paths!")
    playerOneInput = input("Choose your Path: \n Path1: Path PURPLE\n Path2: Path PINK....")
    if playerOneInput == "PURPLE":
        print("You found treasure! You are now rich!")
    else:
        print("You got bitten by a poisonous spider!!! Try Again!")
    while (playerOneInput == "PINK"):
         west()
         break
        


print(start_game())