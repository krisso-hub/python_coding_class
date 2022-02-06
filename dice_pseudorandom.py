'''This is a program that rolls a dice a specified number of times
to get a predictable result.
Author: Ndubuisi  Date: 02/02/2022
'''
import random

def main():
    another = 'Y'
    while (another == 'Y'):
        number_roll = int(input('Enter the number of rolls as an integer: '))
        seed_number = int(input('Enter a seed number above (0): '))
        if (seed_number > 0):
            random.seed(seed_number) # predictable outcome if the seed number is known
        
        for x in range(number_roll):
            result = random.randint(1, 6) + random.randint(1, 6)
            print(result)
        another = input('Another run (Y): ')
main()
