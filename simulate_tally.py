'''A program that roll a pair of dice a specified number of 
   times to tally a list. To compare theorectical probablility.
   Author: Ndubuisi
   Date: 02/09/2022
'''
import random

def main():
    another = 'y'
    expected_prob = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    while another == 'y':
        # prompt a specified number of times
        result_2_dice = [0]*13
        num_roll = int(input('Enter number of rolls desired: '))
        for x in range(num_roll):
            result = random.randint(1, 6) + random.randint(1, 6) # simulate two dice rolls
            result_2_dice[result] += 1
        print('Num-----Total Act    Actual Pct           Expected Pct')
        for i in range(2, 13,1):
            result_pct = result_2_dice[i]/num_roll
            print(f'{i:3}  - {result_2_dice[i]:7}      {result_pct:^7.2%} \
                {expected_prob[i]:^7.2%}')
        another = input('Another run? (y) ')
# call the main() module
main()
    