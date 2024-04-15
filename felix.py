print("in bestand van felix")
import mysql.connector
import algemenefuncties

def methodevanfelix():
    print("op naar de database")
    return "Dit komt van de methode van Felix"

def tweedemethodevanfelix():
    mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ober")

    myresult = mycursor.fetchall()
    eindstring = ""
    for x in myresult:
        print(x[1], " - ", x[3])
        eindstring += x[1]+", "
    return "yes: " + eindstring

    

def derdemethodevanfelix(eenwoord):
    mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )


    mycursor = mydb.cursor()
    sql = "INSERT INTO ober (voornaam, achternaam) VALUES (%s, %s)"
    val = (eenwoord, 'jansen')
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "gelukt"


def nuechtmetjson():
    mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM recept")

    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

# print(derdemethodevanfelix('piet'))

def receptdetailsvanrecept(gid):
    mydb = mysql.connector.connect(
    host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
    user="yc2403admin",
    password="abcd1234ABCD!@#$",
    database="demopythondag"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM recept WHERE id = '"+str(gid)+"'")
    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

def recepttoevoegen2temp(recept):
    mydb = algemenefuncties.verbindingdb()
    mycursor = mydb.cursor()
    sql = "INSERT INTO recept (naam, beschrijving) VALUES (%s, %s)"
    val = (recept["naam"], '')
    mycursor.execute(sql, val)
    mydb.commit()
    return str(mycursor.lastrowid)

def staptoevoegenaanrecept(stap, receptid):
    print(receptid, stap["Stapbeschrijving"])
    return "stap toevoegen"
