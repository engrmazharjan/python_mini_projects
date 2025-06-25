# 📈 Simple Quiz App
# Ask 5 multiple-choice questions.
# Tally and print the score at the end.

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Rome", "D) Berlin"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Leo Tolstoy"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Neptune"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
        "answer": "B"
    },
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        score += 1

print("Your final score is:", score)