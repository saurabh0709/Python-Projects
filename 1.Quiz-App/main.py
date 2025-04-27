import json

def load_questions(filename):
    with open(filename,'r') as file:
        questions = json.load(file)
        return questions
    
# Setting the initial score
score = 0

# Main Menu function
def main_menu(questions):
    print('Welcome to the Python Quiz!')
    print('You will be asked 5 questions. Each question has 4 options and only one is correct.')
    print('You will get 1 point for each correct answer.')
    print('1. Start Quiz')
    print('2. Exit')
    print('Enter your choice: ', end='')
    choice = int(input())
    if choice == 1:
        start_quiz(questions)
    else:
        print('Exited Successfully!')



# Function to accept the user's chosen option
def user_answer():
    chosen_option = input('Please enter the correct option: ')
    # Make the user input uppercase to match with the answer keys
    return chosen_option.upper()

# Function to display the score of the candidate after the end of the quiz
def show_score(score):
    print(f'Your final score is {score} out of {len(questions)}')

# Funtion to start the quiz
def start_quiz(questions):
    global score
    for question in questions:
        print('\n' + question['question'])

        for key, value in question['options'].items():
            print(f'{key}: {value}')

        while True:
            chosen_option = user_answer()
            # Check if a user's answer is valid (A/B/C/D)
            if chosen_option in ['A', 'B', 'C', 'D']:
                if chosen_option == question['answer']:
                    print('✅ Correct Answer!')
                    score += 1
                else:
                    print(f'❌ Incorrect answer! The correct answer is {question["answer"]}.')
                break  # Exit the input loop and move to next question
            else:
                print('Invalid option. Please enter A, B, C, or D.')
    show_score(score)
    
if __name__ == "__main__":
    # Display the main menu and start the quiz
    questions = load_questions('questions.json')
    main_menu(questions)