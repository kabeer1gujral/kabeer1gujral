questions = {
    "What is the capital of France?": "Paris",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the chemical symbol for gold?": "Au"
}

def ask_questions():
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")
    print(f"\nYour final score is {score} out of {len(questions)}.")

def main():
    print("Welcome to the Quiz Game!")
    ask_questions()

if __name__ == "__main__":
    main()
