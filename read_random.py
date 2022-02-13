'''A program that write random numbers to a file, read the random
   numbers and print out the sum, the total and average
   author: Ndubuisi  Date: 02/07/2022
'''
import random

# create and write random numbers to a file
def main():
    f = open('Random.txt', 'w')
    number = input('Enter positive integer number to generate random numbers: ')
    if number.isnumeric():
        number = int(number)
        if (number > 0):
            for no in range(number):
                rand_no = random.randint(1, 500)
                f.write(str(rand_no) + '\n')
            f.close()

# Read random numbers from a file
            with open('Random.txt', 'r') as f: # open file for processing
                sum = 0
                total_num = 0
                num = f.readline()
                while (num != ''):
                    num_no = int(num) # initialize the counter
                    sum += num_no # sums the counter
                    total_num += 1
                    print(f'num_no #{total_num} is {num_no} ')
                    num = f.readline()
                print(f'The total sum is: {sum}')
                print(f'The total number is: {total_num}')
                print(f'The average of the numbers is: {sum / total_num}')
        else:
            print(f'error, enter a positive number greater than zero')
    else:
        print(f'Error, enter a positive integer! ')
    print('The program end')

main()
