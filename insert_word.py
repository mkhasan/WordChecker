
import mysql.connector
from conf import Conf
from native_cpp import *
import conf
import sys
import pandas as pd
from collections import namedtuple



def RemoveNewLine(str):

    length = len(str);
    if str[length-1]=='\n':
        ret = str[:length-1]
    else:
        ret = str

    return ret

def insert_from_file(filename):
    mydb = mysql.connector.connect(
        host = Conf.HSOT,
        user = Conf.USER,
        passwd = Conf.PASSWD,
        database = Conf.DATABASE
    )

    mycursor = mydb.cursor()

    sql = "DROP TABLE IF EXISTS words"
    mycursor.execute(sql)

    sql = "CREATE TABLE words (entry_no INT PRIMARY KEY NOT NULL AUTO_INCREMENT, kor VARCHAR(50) CHARACTER SET EUCKR, eng VARCHAR(50))"
    mycursor.execute(sql)

    f = open(filename, "r")
    contents = f.readlines()
    sql = "INSERT INTO words (kor, eng) VALUES (%s, %s)"
    for x in contents:

        mySplit = split(x)
        #print(mySplit.eng)




        if mySplit.size > 1:


            val = (mySplit.kor, mySplit.eng)

            mycursor.execute(sql, val)
            


    f.close()


    mydb.commit()


def insert_into_db(list, index):
    mydb = mysql.connector.connect(
        host=Conf.HSOT,
        user=Conf.USER,
        passwd=Conf.PASSWD,
        database=Conf.DATABASE
    )

    mycursor = mydb.cursor()


    tableName = "words_" + str(index)


    sql = "DROP TABLE IF EXISTS " + tableName
    mycursor.execute(sql)


    sql = "CREATE TABLE " + tableName
    sql = sql+" (entry_no INT PRIMARY KEY NOT NULL AUTO_INCREMENT, kor VARCHAR(50) CHARACTER SET EUCKR, eng VARCHAR(150))"
    print(sql)
    mycursor.execute(sql)


    sql = "INSERT INTO " + tableName + " (kor, eng) VALUES (%s, %s)"
    for x in list:
        val = (x.kor, x.eng)
        mycursor.execute(sql, val)

    mydb.commit()


class ExcelParser:

    Voca = namedtuple("Voca", ["kor", "eng"])
    def __init__(self, filename, index):
        self.filename = filename
        self.index = index
        self.word = '단어'
        #self.Parse()

    def GetColName(self, k):
        colName = self.word;
        if k == 0:
            return colName

        colName += '.' + str(k)
        return colName

    def GetDictIndex(self, df, colName):
        cols = df.columns
        for x in range(len(cols)-1):
            if cols[x+1] == colName:
                break

        index = int(df.iloc[0][x])
        print(index)
        return (index, x)



    def Parse(self):

        xl = pd.ExcelFile(self.filename)
        sheet_name = xl.sheet_names

        dict = xl.parse(sheet_name)

        # print(len(df1))

        df0 = dict[sheet_name[0]]

        #raise Conf.MyException("test")
        k = 0

        seq = 3
        #print(self.GetColName(seq))

        self.GetDictIndex(df0, self.GetColName(seq))

        #self.index = 6
        targetIndex = 0
        currIndex = 0
        seq = 0
        targetColName = ""
        colName = ""
        currPos = 0
        targetPos = 0

        while currIndex < self.index:
            targetIndex = currIndex
            targetPos = currPos
            targetColName = colName

            colName = self.GetColName(seq)
            (currIndex, currPos )= self.GetDictIndex(df0, colName)
            seq += 1

        startRow = 0
        if currIndex == self.index:
            targetIndex = self.index
            targetPos = currPos
            targetColName = colName
        else:
            startRow = 1


        print("target is %d %d %d %s %s %s" % (self.index, targetIndex, targetPos, targetColName, df0.loc[0][targetPos], df0.loc[0][targetColName]))

        value = -1
        self.list = []
        for x in range(len(df0.index)):
            str = ""
            try:
                #print(df0.loc[x][targetColName])
                value = int(df0.loc[x][targetPos])

            except Exception:
                pass
                #print("Error with %d" % x)

            if value > self.index:
                break
            if value == self.index:
                temp = self.Voca(kor = df0.loc[x][targetPos+1], eng = df0.loc[x][targetPos+2])
                self.list.append(temp)
                #print("(%s %s)" % (df0.loc[x][targetPos+1], df0.loc[x][targetPos+2]))


        return self.list
        #print(df0.columns)


        """
        print(df0.columns)
        colName = '단어';
        val = 1
        colName += '.'+ str(val)
        print(df0.loc[0][colName])

        """

def main():
    #if Conf.READ_FROM_EXCEL_FILE:
    try:
        if len(sys.argv) > 2:
            #print("got it " + sys.argv[1] + sys.argv[2])
            #print("value is %d " % int(sys.argv[2]))
            parser = ExcelParser(sys.argv[1], int(sys.argv[2]))

            list = parser.Parse()
            #print(len(list))
            insert_into_db(list, int(sys.argv[2]))

        else:
            insert_from_file("word_list.txt")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()