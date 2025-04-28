import json

# Load the JSON file containing questions
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

# Quiz Application
def run_quiz(questions):
    score = 0
    user_answers = []

    print("\nWelcome to the Quiz!")
    print(f"There are {len(questions)} questions. Answer carefully!\n")

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}\n")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")
        while True:
            try:
                user_choice = int(input("\nEnter your answer (1-4): "))
                if user_choice < 1 or user_choice > len(q['options']):
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice. Please select a valid option (1-4).")

        user_answer = q['options'][user_choice - 1]
        user_answers.append(user_answer)

        # Check if the answer is correct
        if user_answer == q['answer']:
            score += 1

    print("\nQuiz Completed!")
    print(f"Your score is {score}/{len(questions)}.\n")
    
    print("Review Your Answers:")
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        print(f"Your answer: {user_answers[i]}")
        print(f"Correct answer: {q['answer']}\n")
    return score

# Main function
if __name__ == "__main__":
    questions_file = "quiz_questions.json"
    questions = load_questions(questions_file)
    run_quiz(questions)