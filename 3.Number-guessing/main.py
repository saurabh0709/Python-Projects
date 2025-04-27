import random

# This variable holds the total number of attempts it take to guess the secret number
attempts = 0

# Main Menu function upon the start of the app
def main_menu():

    global attempts

    print('---Welcome to number guessing game---')
    print('You have to guess the number which is between 1 and 20(both inclusive)')
    print('1. Start the game')
    print('2. Exit game')
    
    
    while True:  
        choice  = users_choice()
        if choice == 1:
            secret_num = secret_num_generator()
            checking_guess(secret_num)
            attempts = 0
            want_to_play_again = ask_again_to_play()
            if want_to_play_again == 'N':
               print('Thanks for playing!')
               break

        elif choice == 2:
            print('Thanks for visiting')
            return
        else:
            print('Please enter a valid choice')


#Funtion to ask if user wants to play again
def ask_again_to_play():

    while True:
        want_to_play_again = input('Do you want to play again ?(Y/N)')
        if want_to_play_again.upper() in ['Y','N']:
            return want_to_play_again.upper()
        else:
            print("Enter 'Y' or 'N' !")
            want_to_play_again = input('Do you want to play again ?(Y/N)')

# Function to ask for user's choice whether he wants to play or not
def users_choice():
    choice = int(input('Enter your choice: '))    
    return choice

# Function to generate the secret number
def secret_num_generator():
    secret_num = random.randint(1,20)
    return secret_num

# Function that asks for user's guess
def user_guess():
    guessed_num = int(input('Enter a number between 1 and 20: '))
    return guessed_num

# Function to check if the guess is correct
def checking_guess(secret_num):
    global attempts
    while True:
        guessed_num = user_guess()
        if secret_num == guessed_num:
            attempts += 1
            print(f"congrats✅..you guessed the correct number in {attempts} attempts! ")
            print('\n')
            break
        elif secret_num < guessed_num:
            print('Too high📈')
            attempts += 1
        elif secret_num > guessed_num:
            attempts +=1
            print('Too low📉')

# Driver function
if __name__ == "__main__":
    main_menu()