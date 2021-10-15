'''
This file creates persistence layer
This class is called PersistRowIO and it is created to do file I/O and establish database connection.
getRows() method will read data from csv.
createConn() method is to create database connection.
insert() method is to insert data to database.
delete() method is to delete data from database.
select() method is to retrieve and display data from database.
update() method is to change data in database.
saveRows() method will save data to database. 
plot() method is to plot bar chart for the data from database

Author: Wenbo Ge
Student ID: 040976816
'''

import csv
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from ModelRowDetails import ModelRowDetails

# rowIO is in persistence layer
class PersistRowIO:

    # fist method to perform data read function
    def getRows(self):
        # create list, every row from csv is stored as an object in the list
        covidList = []
        # create string to hold csv file name
        csvName = 'covid19-download.csv'
        rowStop = '2020-04-01'
 
        # handle IO exception
        try:
            with open(csvName) as csvFile:
                csvInput = csv.reader(csvFile, delimiter = ',')
                for r in csvInput:
                        # only want designated columns from csv
                    rowInput = ModelRowDetails(r[0], r[1], r[2], r[3], r[5], r[6], r[7], r[8], r[13], r[15])
                    # only read before 2020-04-01
                    if rowInput.date == rowStop:
                        break
                    else:
                        covidList.append(rowInput)
            return covidList
        except IOError:
            print('No such file')
            return False

    # this method is to create database connection
    def createConn(self):
        try:
            dbConn = mysql.connector.connect(
            host="localhost",
            user="cst8333",
            password="8333",
            database="coviddata"
            )
            print("Database is connected!")
            return dbConn
        except mysql.connector.Error as err:
            print(err)

    # This method is to do SQL select
    def select(self, province):
        # init connection
        conn = self.createConn()
        # init cursor
        myCursor = conn.cursor()
        if province == "":
            # excute select statement
            myCursor.execute("SELECT * FROM covidnumber")
        else:
            # prepare select statement
            sql = "SELECT * FROM covidnumber WHERE prname = %s"
            val = (province,)
            # excute select statement
            myCursor.execute(sql,val)
        result = myCursor.fetchall()
        print("Processing...")
        # print fetched result
        for r in result:
            print(r)

    # This method is to do SQL delete
    def delete(self, province):
        # init connection
        conn = self.createConn()
        # init cursor
        myCursor = conn.cursor()
        if province == "":
            # excute delete statement
            myCursor.execute("DELETE FROM covidnumber")
        else:
            # prepare delete statement
            sql = "DELETE FROM covidnumber WHERE prname = %s"
            val = (province,)
            # excute delete statement
            myCursor.execute(sql,val)
        print("Processing...")
        conn.commit()

    # This method is to do SQL update
    def update(self, province, content):
        # establish db connection
        conn = self.createConn()
        # init cursor
        myCursor = conn.cursor()
        # prepare insert statement
        sql = "UPDATE covidnumber SET pruid = %s, prname = %s, prnameFR = %s, date = %s, numconf = %s, numprob = %s, numdeath = %s, numtotal = %s, numtoday = %s, ratetotal = %s WHERE prname = %s"
        val = (content.pruid, content.prname, content.prnameFR, content.date, content.numconf, content.numprob, content.numdeath, content.numtotal, content.numtoday, content.ratetotal, province)
        # excute insert statement
        myCursor.execute(sql,val)
        # commit change
        conn.commit()

    # this method is to insert data into database
    def insert(self, row):
        # establish db connection
        conn = self.createConn()
        # init cursor
        myCursor = conn.cursor()
        # prepare insert statement
        sql = "INSERT INTO covidnumber (pruid, prname, prnameFR, date, numconf, numprob, numdeath, numtotal, numtoday, ratetotal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row.pruid, row.prname, row.prnameFR, row.date, row.numconf, row.numprob, row.numdeath, row.numtotal, row.numtoday, row.ratetotal)
        # excute insert statement
        myCursor.execute(sql,val)
        # commit change
        conn.commit()

    # this method is to save data into table in database
    def saveRows(self, rows):
        # establish db connection
        conn = self.createConn()
        # insert data but skip first row (which is header row)
        for index, r in enumerate(rows[1:]):
            # init cursor
            myCursor = conn.cursor()
            # prepare insert statement
            sql = "INSERT INTO covidnumber (pruid, prname, prnameFR, date, numconf, numprob, numdeath, numtotal, numtoday, ratetotal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (r.pruid, r.prname, r.prnameFR, r.date, r.numconf, r.numprob, r.numdeath, r.numtotal, r.numtoday, r.ratetotal)
            # excute insert statement
            myCursor.execute(sql,val)
            # commit change
            conn.commit()
            print(str(index+1) + " record inserted...")

    # this method is to map data
    def plot (self, province):
        # init connection
        conn = self.createConn()   
        if not province:
            # prepare select statement
            sql = "SELECT prname, sum(numconf) as TotalNumber FROM covidnumber group by prname"
        elif len(province) == 1:
            # prepare select statement
            sql = "SELECT prname, sum(numconf) as TotalNumber FROM covidnumber where prname = \'{}\' group by prname".format(province[0])
        else:
            # use tuple to split list
            t = tuple(province)
            # prepare select statement
            sql = "SELECT prname, sum(numconf) as TotalNumber FROM covidnumber where prname in {} group by prname".format(t)
        # plot a bar chart to display provinces and their total numbers based on user's selection
        df = pd.read_sql(sql, conn)
        df.plot(kind="bar", x="prname", y="TotalNumber", title = "Covid Confirmed Cases Before 2020-04-01")
        plt.show()
