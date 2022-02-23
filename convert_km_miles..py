'''A program that the convert KM to Miles with try and 
    except catch using GUI
    Author: Ndubuisi,  Date: 02/21/2022
'''
from breezypythongui import EasyFrame
import math
class DemoKMtoMiles(EasyFrame):  # create the class
    def __init__(self):   # set initial state
        EasyFrame.__init__(self,title="Convert KM to Miles") # create window

        # create the window with header
        # add single label and the field for the input
        self.setResizable(True) # allow users to resize window
        self.addLabel(text ="Input KiloMeter", row=0, column=0)
        self.inputField = self.addFloatField(value=0.0, row=0, column=1, width=10)

        #Add single label and field for the output
        self.addLabel(text ="Miles", row=1,column=0)
        self.outputField = self.addFloatField(value=0.0,row=1,column=1, width=8, precision=2, state="readonly")

        # the command button with event handler method
        self.addButton(text="command",row=2,column=0,columnspan=2,command=self.computeMiles)
        #add an exit button part of final project
        self.quit_button= self.addButton(text="QUIT",row=2,column=2,command=self.master.destroy)

       
        # method to handle event
    def computeMiles(self):
        try:   #error handling
            number = self.inputField.getNumber()
            cm = number * 100000
            miles = cm /2.54 / 12 /5200
            result = miles
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR", message= "Input must be an integer >= 0")
def main():
    DemoKMtoMiles().mainloop()
if __name__== "__main__":
    main()


            
             
