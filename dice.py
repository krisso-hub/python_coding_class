
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = 0   # initialize roll integer type
    def roll(self):
        self.value = random.randint(1,self.sides)
    def get_roll(self):
        return self.value
    def get_sides(self):
        return self.sides
    def set_sides(self,sides):
        self.sides = sides
def main():
# create an object from the Die class
    my_diel = Die()
    print('Initial Value is   ', my_diel.get_roll())
    print('sides              ', my_diel.get_sides())
    # roll the object my_Die
    for i in range (10):
        my_diel.roll()  # roll die
        print('Value after roll  ', i+1, ' is ', my_diel.get_roll())
    my_diel2 = Die(10)
    print('Initial Value is  ', my_diel2.get_roll())
    print('Sides      ', my_diel2.get_sides())
    # roll the object my_Die
    for i in range (10):
        my_diel2.roll()  # roll die.
        print('Value after roll ', i+1, 'is ', my_diel2.get_roll())
        # test mutator set-sides simulate a coin
    my_diel2.set_sides(2)
    print('Sides      ', my_diel2.get_sides())
    for i in range (10):
        my_diel2.roll()   #roll die
        print('Value after roll ', i+1, 'is ', my_diel2.get_roll())

if __name__ =='__main__':
    main()
