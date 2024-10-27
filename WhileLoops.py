import random
number = random.randint(1, 100)
guess = None

while guess != number:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("You have guessed the correct number")
    except Error:
        print("invalid input")
