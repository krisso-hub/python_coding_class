# day 7 Roll a pair of dice a specified number of times
# track and store results in a list
# John Treacy 2/10/2021
def main():
    import M07_Ch09_Die_Class_WSides
    Die1 = M07_Ch09_Die_Class_WSides.Die()
    Die2 = M07_Ch09_Die_Class_WSides.Die()
    another = 'y'
    # define tuple for expected values.
    ExpectedProb = (0,0,1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36)
    # dice roll 2-12 element of 13 Theoretical probabilities
    import random  # random number generator for dice
    while (another == 'y'):
        NumRoll = int(input('Enter number of 2-dice rolls as an integer: '))
        result2Dice = [0]*13  # create list of 13 elements init to zero.
        for x in range(NumRoll):    # loop through experiment
            result = random.randint(1,6)+random.randint(1,6) # simulate roll of 2 dice
            Die1.roll()
            Die2.roll()
            result = Die1.get_roll() + Die2.get_roll()

 #           print(result)   # diagnostics only verify works for small comment on big
            result2Dice[result] += 1
        print('Num----Total Act   Actual Pct          Expected Pct')
        for i in range(2,13,1):
            resultPct = result2Dice[i]/NumRoll  # calculate percent
            print(f'{i:3} - {result2Dice[i]:7}    {resultPct:^7.2%}   \
                 {ExpectedProb[i]:^7.2%}')  # Pretty professional print
        another = input('Another run? (y)')
# call main() module
main()
