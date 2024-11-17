# Simple Quiz Game

def ask_question(question, answer_options, correct_answer):
    """
    This function asks a multiple-choice question, and checks if the answer is correct.
    
    Parameters:
    - question: The question to ask.
    - answer_options: List of possible answers.
    - correct_answer: The correct answer.
    
    Returns:
    - A boolean indicating if the answer was correct.
    """
    print(question)
    
    # Display options
    for i, option in enumerate(answer_options, 1):
        print(f"{i}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Your answer (1, 2, 3, or 4): "))
    
    # Check if the answer is correct
    if answer_options[user_answer - 1].lower() == correct_answer.lower():
        print("Correct! 🎉")
        return True
    else:
        print("Oops! The correct answer is:", correct_answer)
        return False

def play_quiz():
    # Define the questions and answers
    questions = [
        {"question": "What is the capital of France?", 
         "options": ["Berlin", "Madrid", "Paris", "Rome"], 
         "answer": "Paris"},
        {"question": "What is 5 + 7?", 
         "options": ["10", "12", "15", "17"], 
         "answer": "12"},
        {"question": "Which programming language is known as the snake language?", 
         "options": ["Java", "Python", "Ruby", "C++"], 
         "answer": "Python"}
    ]
    
    # Initialize score
    score = 0
    
    # Loop through all questions
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1
    
    # Display final score
    print(f"\nYour final score is: {score}/{len(questions)}")

# Start the game
play_quiz()
