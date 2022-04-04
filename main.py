import random
import sys
play = 'y'
while play == 'y':
    player = input("Rock Paper Scissors shoot! ").lower()
    rng = random.randint(1,3)
    if player == 'r' or 'rock':
        if rng == 1:
            print("Tie game!")
        elif rng == 2:
            print("Paper covers rock!")
        else:
            print("Rock smashes scissors!")
    play = input("Play again? (y/n ")
    