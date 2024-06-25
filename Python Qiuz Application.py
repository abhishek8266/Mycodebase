def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for questions, correct_answer in questions:
        print(questions)
        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is '{correct_answer}'.")

        print()

    print(f"You've completed the quiz!")
    print(f"Your final score is {score} out of {total_questions}.")


quiz_questions = [
    ("What is the capital of India?", "Delhi"),
    ("Who developed 'Python'?", "Guido van Rossum"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who is the highest mountain in India?", "Kanchenjunga"),
    ("What is the powerhouse of the cell?", "Mitochondria")
]


run_quiz(quiz_questions)
