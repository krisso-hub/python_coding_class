''' A program that request two decimal place number
from users, muiltiplies them and return the result to the user.
written by: Ndubuisi Asogwa 01/24/22
'''
def muiltiply_number():
# Muiltiplies any two floating numbers
    num1 = float(input('write a decimal place number: '))
    num2 = float(input('write a second decimal place number: '))
    num = num1 * num2
# The result of multiples of any two floating numbers
    print(f'The muiltiple of the two numbers is {num}')
muiltiply_number()