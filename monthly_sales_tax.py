'''A program that ask client for amount of sales recorded for 
    a month and compute the county sales tax, state sales
    tax and total sales tax
    Author: Ndubuisi,   Date: 02/26/2022
'''
# tax rate declared
county_tax_rate = 0.025
state_tax_rate = 0.05

def sales_tax():
    Sales = input('Enter sales record for the month: $')
    if Sales.isnumeric():
        sales = int(Sales)
        county_tax = sales * county_tax_rate
        state_tax = sales * state_tax_rate
        total_tax = county_tax + state_tax
        print(f'The amount of county tax is ${county_tax}')
        print(f'The amount of state tax is ${state_tax}')
        print(f'The amount of total sales tax is ${total_tax}')
    else:
        print('Error, Enter a valid sale record')

sales_tax()
