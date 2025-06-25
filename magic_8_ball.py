# 💬 Magic 8-Ball
# Ask any yes/no question.
# Program responds with one of several random answers like “Yes”, “No”, “Ask again later”.

import random

responses = [
    "Yes",
    "No",
    "Ask again later",
    "Definitely",
    "Absolutely not",
    "Maybe",
    "It is certain",
    "Very doubtful",
    "Without a doubt",
    "My sources say no",
    "Outlook not so good",
    "Yes, in due time",
    "No way",
    "It is decidedly so",
    "You may rely on it",
    "As I see it, yes",
    "Better not tell you now",
    "Cannot predict now",
]

input("Ask your yes/no question: ")
print("Magic 8-Ball says:", random.choice(responses))