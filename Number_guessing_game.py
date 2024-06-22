import random
def Number_guessing_game(a, b):
    r1 = random.randint(a, b)
    r2 = int(input("Guess a random number between {} and {}: ".format(a, b)))
    if r2 == r1:
        print("Well done! You guessed right.")
    elif r2 > r1:
        print("You guessed too high!")
    else:
        print("You guessed too low!")
