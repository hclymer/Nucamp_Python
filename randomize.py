import random 

pips = random.randint(1,6)
print("You roll the die... it lands with", pips, "pip showing.")

prizes = ["a car", "$10000", "a pony", "$50000"]
prize_won = random.choice(prizes)
print("You spin the wheel of fortune... It lands on a prize of", prize_won, "!!")

cards = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards)