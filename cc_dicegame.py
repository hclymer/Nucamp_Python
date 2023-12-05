import random


high_score = 0


def dice_game():
    global high_score
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("You roll a...", dice1)
    print("You roll a...", dice2)
    total = dice1 + dice2
    print("You have rolled a total of...", total)
    if total >= high_score:
        high_score = total
        print("New High Score!\n")


while True:
    print("Current High Score:", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice:")
    if choice == "1":
        dice_game()
    elif choice == "2":
        break
