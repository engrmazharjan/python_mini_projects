import random

target = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = input("Enter your guess (1-100) or 'Quit' to exit: ")
    if(guess == "Quit"):
        print("Game Over : You quit the game")
        break
    guess = int(guess)
    attempts += 1

    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {target} in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {target}.")

    