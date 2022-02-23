'''A program that do arithmetic of addition, subtraction
    division and multiplication using try and 
    except catch on GUI
    Author: Ndubuisi,  Date: 02/21/2022
'''
from breezypythongui import EasyFrame
import math
class Arithmetic(EasyFrame):  # create the class
    def __init__(self):   # set initial state
        EasyFrame.__init__(self,title="Arithmetics") # create window

        # create the window with header
        # add single label and the field for the input
        self.setResizable(True) # allow users to resize window
        self.addLabel(text ="Input Ist Number", row=0, column=0)
        self.inputField1 = self.addFloatField(value=0, row=0, column=1, width=10)

        self.addLabel(text ="Input 2nd Number", row=1, column=0)
        self.inputField2 = self.addFloatField(value=0, row=1, column=1, width=10)

        #Add single label and field for the output
        self.addLabel(text ="Total", row=2,column=1)
        self.outputField = self.addFloatField(value=0.0,row=2,column=2, width=8, precision=2, state="readonly")

        # the command button with event handler method
        #self.addButton(text="command",row=2,column=0,columnspan=2,command=self.computeMiles)
        #add an exit button part of final project
        self.quit_button= self.addButton(text="QUIT",row=2,column=4,command=self.master.destroy)

        self.addButton(text ="Add",row=6,column=0, command=self.add)
        self.addButton(text="Subtract", row=6,column=1, command= self.subtract)
        self.addButton(text="Multiply", row=6,column=3, command= self.multiply)
        self.addButton(text = "Divide", row=6, column=4, command= self.divide)
        # method to handle event

    def multiply(self):
        try:   #error handling
            number1 = self.inputField1.getNumber()
            number2 = self.inputField2.getNumber()
           
            result = number1 * number2
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")
    
    def divide(self):
        try:   #error handling
            number1 = self.inputField1.getNumber()
            number2 = self.inputField2.getNumber()
           
            result = number1 / number2
            self.outputField.setNumber(result)
        except ZeroDivisionError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")
        except ValueError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")

    def add(self):
        try:   #error handling
            number1 = self.inputField1.getNumber()
            number2 = self.inputField2.getNumber()
           
            result = number1 + number2
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")
    def subtract(self):
        try:   #error handling
            number1 = self.inputField1.getNumber()
            number2 = self.inputField2.getNumber()
           
            result = number1 - number2
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")
def main():
    Arithmetic().mainloop()
if __name__== "__main__":
    main()


            
             
