import random
def number_guessing_game():
    targetNumber = random.randint(1, 100)
    play = input('Do you want to play guessing number game? y/n').strip().lower()


    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        try:
            return True
        except:
            print('')
    play = input()
    return True
