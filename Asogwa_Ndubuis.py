'''This program calculate the total cost of a meal in a restarant
adding the meal cost, sales tax and tips together
author: Ndubuisi Asogwa, date:01/30/22
'''

def total_cost_meal():
# Requesting customer to enter the price of the meal
    sale_price = int(input('Enter the price of the meal: '))
    sales_tax = 0.07 * sale_price
    meal_tip = 0.18 * sale_price
    total_sale = sale_price + sales_tax + meal_tip
    print(f'Your total cost with 18% tips is ${total_sale}')
total_cost_meal()