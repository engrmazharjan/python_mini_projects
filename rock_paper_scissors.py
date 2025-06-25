# 🧠 1. Rock, Paper, Scissors Game
# User plays against the computer.
# Computer randomly picks rock/paper/scissors.
# Simple comparison logic.

import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

user_choice = input("Enter your choice (rock, paper, scissors) or 'Quit' to exit: ").lower()

if user_choice == "Quit":
    print("Game Over: You quit the game.")
elif user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")    