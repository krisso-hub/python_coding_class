'''A program that convert a binary digits to its equivalent
in decimal number
author: Ndubuisi  Date: 02/04/2022
'''

def binary_decimal():
# User enter any number of binary digits
    bit_string = input('Enter bits of strings: ')
    decimal = 0
    exponent = len(bit_string) - 1
    for digit in bit_string:
        
        decimal = decimal + int(digit) * 2**exponent
        exponent -= 1
    print(decimal)

binary_decimal()
