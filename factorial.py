'''A program that calculate a factorial of any 
given positive number and produce the result.
Author: Ndubuisi  Date: 02/05/2022
'''
# A prompt requesting integer value from user
number = input('Enter any positive integer for n!: ')
num = 1 # result initiliazed
if number.isnumeric():
    integer = int(number)
    while (integer) > 0:
        num = num * (integer)
        integer -= 1
    print(f'The integer {number}! is: {num}')
else:
    print('Error, enter positive integer for n!')