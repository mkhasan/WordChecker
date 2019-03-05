
import mysql.connector
from conf import Conf
import numpy as np

class Finder:
    def __init__(self, isRandom):
        self.Reload()
        self.Reset(isRandom)

    def Reload(self):
        mydb = mysql.connector.connect(
            host=Conf.HSOT,
            user=Conf.USER,
            passwd=Conf.PASSWD,
            database=Conf.DATABASE
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM "+Conf.TABLENAME
        mycursor.execute(sql)
        self.results = mycursor.fetchall()
        #print(self.results)


    def Reset(self, _isRandom):
        self.isRandom = _isRandom
        arr = np.arange(len(self.results))
        if _isRandom == True:
            arr = np.random.permutation(arr)
        self.permutation = arr
        self.index = -1

    def GetNext(self, forward):
        if self.index == -1:
            self.index = 0;
        else:
            if forward:
                self.index = (self.index+1)%(len(self.permutation))
            else:
                self.index = (self.index - 1 + len(self.permutation)) % (len(self.permutation))

        ret = self.results[self.permutation[self.index]]
        return (ret, self.index)


