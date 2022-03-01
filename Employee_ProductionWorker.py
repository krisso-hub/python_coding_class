'''A subclass of employee production worker
    defined here
    Author: Ndubuisi,   Date: 02/28/2022
'''
class Employee:
    def __init__(self, name, number):
        self.__name = name         # Initiliaze instance variable
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number
class ProductionWorker(Employee):   # subclass of Employee
    def __init__(self, name, number, shift, hrRate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__hrRate = hrRate
    def get_shift(self):          # accessor of subclass production worker
        return self.__shift
    def get_hrRate(self):
        return self.__hrRate
    def set_shift(self, shift):    # mutator methods here subclass
        self.__shift = shift
    def set_hrRate(self, hrRate):
        self.__hrRate = hrRate


        pass