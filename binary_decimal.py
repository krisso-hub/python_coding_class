'''A program that convert a binary digits to its equivalent
in decimal number and vice versal
author: Ndubuisi  Date: 02/04/2022
'''
# converting from binary to decimal digits
def binary_decimal():
# User enter any number of binary digits
    bit_string = input('Enter bits of strings: ')
    decimal = 0
    exponent = len(bit_string) - 1
    for digit in bit_string:
        
        decimal = decimal + int(digit) * 2**exponent
        exponent -= 1
    print(f'The binary digits of {bit_string} is equivalent to decimal digit of {decimal}')

binary_decimal()

# converting from decimal to binary digits
def decimal_binary():
    decimal = ''
    while True:
        
        decimal = (input('Enter an integer number: '))
        if decimal == '':
            break
        elif decimal.isdigit():
            decimal = int(decimal)
            if (decimal) == 0:
                print(decimal)
            else:
                bit_string = ''
                print('Quotient Remainder Binary')
                while decimal > 0:
                    reminder = decimal % 2
                    decimal = decimal // 2
                    bit_string = str(reminder) + bit_string
                    print('%3d%9d%13s' % (decimal, reminder, bit_string))
                print(f'The binary representation is {bit_string}')
        else:
            print(" Error Enter a valid integer number")

decimal_binary()