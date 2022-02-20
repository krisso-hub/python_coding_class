'''This a program that request users to enter a positive number
    greater than one, And the program will list all the prime
    numbers below the number entered by the user
    Author: Ndubuisi,   Date: 02/20/22
'''
# list range of prime numbers
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# list range of numbers from 2 upwards
def check_prime():
    num = (input('Enter a positive number greater than one: '))
    if num.isnumeric():
        num = int(num)
        if num > 1:
            print('The list of prime numbers:')
            list_numbers = list(range(2, num +1))
            for nu in list_numbers:
# verify if the list of numbers are a prime or not
                if nu in prime(2, num):
                    
                    print(nu, end=', ')
        else:
            print('Error, enter a positive number greater than one')
    else:
        print('Error, enter a positive integer greater than one')
        
check_prime()
