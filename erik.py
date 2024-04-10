
import mysql.connector
import onzepython

def methodeerik(tweeword, driewoord):
    mydb = onzepython.mydb

    mycursor = mydb.cursor()
    sql = "INSERT INTO recept (naam, aantalsterren) VALUES (%s, %s)"
    val = (tweeword, driewoord)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "Je recept is aangemaakt!" 



def staptoevoegen(stap):

    mydb = onzepython.mydb

    mycursor = mydb.cursor()
    sql = "INSERT INTO dummy_stappen (stap) VALUES (%s)"
    val = [stap]
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "Je stap is toegevoegd!" 

