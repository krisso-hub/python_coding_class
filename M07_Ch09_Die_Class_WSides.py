"""
      M07_ch09_Die_Class_WSides.py
#  Chapter 9 Classes and OOP For the SDEV140 Fall 2021 1st 8 weeks.
#  Die_Class_WSides.py
# die class simulator.
#          private variable value
#          Methods roll() - Physical rolling of 6-sided die (random.randint() )
#                 get_roll - returns roll value.
                  get_sides - accessor returns number of sides of Die object.
                  set_sides(sides) - mutator to set number of sides.
                  __init__ - optional sides parameter (default 6)
"""
import random  # Get system random number for
class Die:     # Return uniform distribution of integers 1 through 6
    def __init__(self,sides=6):
        self.sides = sides
        self.value = 0       # initialize roll  integer type
    def roll(self):
        self.value= random.randint(1,self.sides)
    def get_roll(self):
        return self.value
    def get_sides(self):
        return self.sides
    def set_sides(self,sides):    # mutator to set sides
        self.sides = sides
def main():      # Class test from own program 
#        create an object from the Die class
    my_die1 = Die()       # object created default 6 sides
    print('Initial Value is    ', my_die1.get_roll())
    print('Sides               ', my_die1.get_sides())
      # roll the object my_Die
    for i in range (10):
        my_die1.roll()  # roll die.
        print('Value after roll ',i+1, ' is ', my_die1.get_roll())
    my_die2 = Die(10)       # object created 10 sides
    print('Initial Value is    ', my_die2.get_roll())
    print('Sides               ', my_die2.get_sides())
      # roll the object my_Die
    for i in range (10):
        my_die2.roll()  # roll die.
        print('Value after roll ',i+1, ' is ', my_die2.get_roll())
      # test mutator set_sides simulate a coin
    my_die2.set_sides(2)
    print('Sides               ', my_die2.get_sides())
    for i in range (10):
        my_die2.roll()  # roll die.
        print('Value after roll ',i+1, ' is ', my_die2.get_roll())
# Call main function direct for class test.
if __name__=='__main__':
    main()
