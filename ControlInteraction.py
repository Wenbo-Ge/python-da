'''
This file creates controller layer
This class is called ControlInteraction and it will control and doing 
interaction jobs between persistence, view and model layers

Author: Wenbo Ge
Student ID: 040976816
'''

from PersistRowIO import PersistRowIO


class ControlInteraction:
    # init an objects from PersistRowIO classes
    dataControl = PersistRowIO()
    
    # declare a list variable to store data
    dataList = []

    # Reload the data from the dataset, replacing the in-memory data.
    def reload(self):
        self.dataList.clear()
        self.dataList = self.dataControl.getRows()
        # then return the list
        return self.dataList

    # Persist the data from memory to the disk as a comma-separated file, writing to a new file
    def persist(self):
        self.dataControl.saveRows(self.dataList)

    # Select and display either one record, or display multiple records from the in-memory data
    def display(self, province):
        self.dataControl.select(province)
       
    # Create a new record and store it in the simple data structure in memory
    def create(self, content):
        self.dataControl.insert(content)

    # Select and edit a record held in the simple data structure in memory
    def edit(self, province, content):
        self.dataControl.update(province, content)

    # Select and delete a record from the simple data structure in memory
    def delete(self, province):
        self.dataControl.delete(province)

    # Select and map records from db
    def map(self, province):
        self.dataControl.plot(province)