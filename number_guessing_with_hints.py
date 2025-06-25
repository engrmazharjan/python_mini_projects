# 🎯 3. Number Guessing Game with Hints
# Difficulty levels (Easy: 1–10, Medium: 1–50, Hard: 1–100).
# Gives closer/farther hints like "Very close!" or "Far off!"

import random

target = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (1-100) or 'quit' to exit: ").lower()

    if guess == "quit":
        print("Game Over: You quit the game.")
        break

    if not guess.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    
    guess = int(guess)
    attempts += 1
    diff = abs(target - guess)
    
    if guess == target:
        print(f"Congratulations! You've guessed the number {target} in {attempts} attempts.")
        break
    elif guess < target:
        print("Too low!", end=" ")
    else:
        print("Too high!", end=" ")
    
    if diff <= 5:
        print("Very close!")
    elif diff <= 15:
        print("Close!")
    else:
        print("Far off!")
