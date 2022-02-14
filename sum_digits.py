'''A program that request series of numerical input
  for user, add up each digits and return the total sum
  Author: Ndubuisi   Date: 02/13/2022
'''

# summation of a series of numbers
def main():
    sum = 0
    string_digits = input('Enter a series of digits: ')
    if string_digits.isdigit():
        for digit in string_digits:
            sum = sum + int(digit)
        print(f'The total sum of the digits is {sum}')
    else:
        print("Error, enter a digits number: ")
main()