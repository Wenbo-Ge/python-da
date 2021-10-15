'''
This file creates view layer
This class is called ViewPrint and it will display options and information rended into console 

Author: Wenbo Ge
Student ID: 040976816
'''

from ModelRowDetails import ModelRowDetails
from ControlInteraction import ControlInteraction

class ViewPrint:
    
        
    # init an object from ControlInteraction classes
    viewDisplay = ControlInteraction()

    # define a method to print menu
    def menuPrint(self):
        # print menu
        print("Input r to reload\nInput p to persist\nInput s to display\nInput c to create\nInput e to edit\nInput d to delete\nInput m to create bar chart\nInput x to exit\n\n")
        # loop the menu after user made input
        while(True):
            selection = input()
            # do the interaction based on user's input
            self.action(selection)
            # if there is an x, then exit
            if selection == 'x':
                break
            else:
                # then print menu again
                print("Input r to reload\nInput p to persist\nInput s to display\nInput c to create\nInput e to edit\nInput d to delete\nInput m to create bar chart\nInput x to exit\n\n")
            

    # define a method to process the selection
    def action (self, selection):
        # process reload function
        if selection == 'r':
            self.viewDisplay.reload()
            print("Reload is done!\n\n")

            # process persist function
        elif selection == 'p':
            self.viewDisplay.persist()
            print("Data is loaded to database!\n\n")

            # prcess display function
        elif selection == 's':
            print("Show all please hit Enter key, show provincial records, input province name:")
            province = input()
            self.viewDisplay.display(province)
            print("Records are printed!\n\n")
    
            # process create function
        elif selection == 'c':
            print("Input record info:\nFollowing information are automatically input for you: \npruid: 000, prname: test, prnameFR: test, date: 0000-00-00, numconf: 0, numprob: 0, numdeath: 0, numtotal: 0, numtoday: 0, ratetotal: 0")
            rowInput =  ModelRowDetails('000', 'test', 'test', '0000-00-00', '0', '0', '0', '0', '0', '0')
            self.viewDisplay.create(rowInput)
            print("Record is created!\n\n")

            # process edit function
        elif selection == 'e':
            print("This process will change target record to\npruid: 000, prname: AAA, prnameFR: AAA, date: 0000-00-00, numconf: 0, numprob: 0, numdeath: 0, numtotal: 0, numtoday: 0, ratetotal: 0\nWhich province you want to change?")
            rowInput =  ModelRowDetails('000', 'AAA', 'AAA', '0000-00-00', '0', '0', '0', '0', '0', '0')
            province = input()
            self.viewDisplay.edit(province, rowInput)
            print("Edit is done\n\n")

            # process delete function
        elif selection == 'd':
            print("Delete all please hit Enter key, delete provincial records, input province name:")
            province = input()
            self.viewDisplay.delete(province)
            print("Records are deleted!\n\n")
            
            # bar chart function
        elif selection == 'm':
            province = list(map(str, input("Map all please hit Enter key, map provincial records, input province names separate by space: ").split()))
            print("Provinces to map: ", province)
            print("Length of list: ", len(province))
            self.viewDisplay.map(province)
            print("Records are mapped!\n\n")
        elif selection == 'x':
            print("Thank you! Program ended!")
        else:
            print("Wrong input, try again")
            




