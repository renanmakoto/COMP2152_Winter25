import random
def number_guessing_game():
    targetNumber = random.randint(1, 100)
    play = input('Do you want to play guessing number game? y/n').strip().lower()
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        try:
            userGuess = int(input('Enter your guess: '))
            attempts += 1
            if userGuess < targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print('Too low, but close. Try again.')
                else:
                    print('Too low. Try again.')
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print('Too high, but close. Try again.')
                else:
                    print('Too high')
            else:
                print(f'Congratulations you have guessed it in {attempts} attempt.')
                return
        except ValueError:
            print('Invalid input! Please, enter a number between 1 and 100')
    print(f'Game over! The target number was {targetNumber}.')   
number_guessing_game()
