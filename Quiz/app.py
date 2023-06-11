import json

def load_questions_from_file(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def present_question(question):
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer - 1  # This adjusting the answer to be on a zero-based index
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_answer(question, answer):
    if question['correct_answer'] == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1} of {total_questions}:")
        present_question(question)
        user_answer = get_user_answer()
        score += evaluate_answer(question, user_answer)
    
    print(f"\nQuiz completed! Your score: {score}/{total_questions}")

# Example usage
questions = load_questions_from_file('questions.json')  # Assuming questions are stored in a JSON file
play_quiz(questions)
