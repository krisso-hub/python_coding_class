'''A program that write random numbers in to file and displays
    all the numbers to a console
    author: Ndubuisi   Date: 02/13/2022
'''

import random
# Write ramdom numbers to a file
f = open('randonfile.txt', 'w')
number = input('Enter a positive random number to generate: ')
if number.isdigit():
    num = int(number)
    if (num > 0):
        for no in range(num):
            rand_no = random.randint(1, 500)
            f.write(str(str(rand_no) + '\n'))
        f.close()

# Read contents from the same file displays to the console
        with open('randonfile.txt', 'r') as f:
            num = f.readline()
            while (num != ''):
                num = f.readline()
                print(num, end='')
    else:
        print('Error, enter a positive greater than 0')
else:
    print('Error, enter a postive digit number: ')