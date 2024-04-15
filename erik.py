
import mysql.connector
import onzepython
import algemenefuncties

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

def receptnaamtoevoegen(naam):

    mydb = onzepython.mydb

    mycursor = mydb.cursor()
    sql = "INSERT INTO dummy_stappen (naam) VALUES (%s)"
    val = [naam]
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "Je recept naam is toegevoegd!" 

def ingredienttoevoegenaanrecept(ingredient, receptid):
    print(receptid, ingredient["naam"])
    return "ingredient toevoegen"