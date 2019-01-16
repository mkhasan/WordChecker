
import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="test123",
        database = "TEST_DB"
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
        print(len(fields))
        #print(fields[1])
        val = (fields[0], fields[1])
        mycursor.execute(sql, val)

    f.close()


    mydb.commit()

    test = "손"

    print(test)


if __name__ == '__main__':
    main()