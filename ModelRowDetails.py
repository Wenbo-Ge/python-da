'''
This file creates model layer
an object class called ModelRowDetails is created to store data in every row

Author: Wenbo Ge
Student ID: 040976816
'''

# rowDetails is in model layer
class ModelRowDetails:
    def __init__(self, pruid, prname, prnameFR, date, numconf, numprob, numdeath, numtotal, numtoday, ratetotal):
        self.pruid = pruid
        self.prname = prname
        self.prnameFR = prnameFR
        self.date = date
        self.numconf = numconf
        self.numprob = numprob
        self.numdeath = numdeath
        self.numtotal = numtotal
        self.numtoday = numtoday
        self.ratetotal = ratetotal

    