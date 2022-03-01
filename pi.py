'''A guessing game program that guides users to guess
    the correct number in a random of numbers of 1 to 
    100
    Author: Ndubuisi,  date: 02/26/2022
'''
import random

def guess_game():
    # variable declaration for secret number and loop
    secret_number = random.randint(1, 101)
    start = 'yes'
    while start == 'yes':
    # A counter set to monitor the number of guesses
        for guess_taken in range(1, 50):
            Guess = input('Guess a secret number between (1 and 100):  ')
            if Guess.isnumeric():
                guess = int(Guess)
                if guess < secret_number:
                    print('your guess number is low, try again')

                elif guess > secret_number:
                    print('your guess number is high, try again')
                elif guess == secret_number:
                    print(f'Congrat! you got the correct number ({secret_number}) in {guess_taken} attempts')
                    break
                else:
                    print(f'Naa! You did not get the correct number in {guess_taken} attempts')
                
            else:
                print('Error, Enter valid number')
        start = input('Enter (yes) to play again or any letter to end: ')
        
    print('The has game ended')
guess_game()