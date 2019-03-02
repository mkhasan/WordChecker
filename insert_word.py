
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
        print("%s size is %d" % (x, len(fields)))
        #print("%s %d" % (fields[1], int(fields[1][len(fields[1])-1])))
        #index = len(fields[1])
        if len(fields) > 1:

            str = ""
            for count in range(len(fields)-1):
                #print(fields[count+1])
                str = str + " " + fields[count+1]

            val = (fields[0], RemoveNewLine(str))

            mycursor.execute(sql, val)

    f.close()


    mydb.commit()




if __name__ == '__main__':
    main()