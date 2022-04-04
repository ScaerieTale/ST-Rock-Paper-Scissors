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
    elif player == 'p' or 'paper':
        if rng == 1:
            print("Paper covers rock!")
        elif rng == 2:
            print("Tie game!")
        elif rng == 3:
            print("Scissors cuts paper!")
    elif player == 's' or 'scissors':
        if rng == 1:
            print("Rock smashes scissors!")
        elif rng == 2:
            print("Scissors cuts paper!")
        elif rng == 3:
            print("Tie game!")
    play = input("Play again? (y/n ")
    