
import mysql.connector
from conf import Conf

def RemoveNewLine(str):
    length = len(str);
    if str[length-1]=='\n':
        ret = str[:length-1]
    else:
        ret = str

    return ret

def main():
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

    f = open("word_list.txt", "r")
    contents = f.readlines()
    sql = "INSERT INTO words (kor, eng) VALUES (%s, %s)"
    for x in contents:
        fields = x.split(" ")
        #print(len(fields))
        index = len(fields[1])
        if fields[1][index-1] == '\r':
            print("%s" % fields[1][:index-1])

        val = (fields[0], RemoveNewLine(fields[1]))
        mycursor.execute(sql, val)

    f.close()


    mydb.commit()

    test = "손"

    print(test)


if __name__ == '__main__':
    main()