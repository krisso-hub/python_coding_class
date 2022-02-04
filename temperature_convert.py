'''This program convert celcius temperature to its equivalent
in fahrenheit.
author: Ndubuisi Asogwa, Date: 01/30/22
'''
def convert_celcius_fahrenheit():
# Requsting user to enter a temperature in celcius for convertion to fahrenheit
    celcius_temp = int(input('Enter a temperature in celcius: '))
    fahrenheit_temp = int((9/5 * celcius_temp) + 32)
    print(f'The celcius of {celcius_temp} degree is equivalent to fahrenheit of {fahrenheit_temp} degree')

convert_celcius_fahrenheit()