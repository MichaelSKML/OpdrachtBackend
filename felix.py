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
#    mycursor.execute("SELECT * FROM recept LEFT JOIN stappen ON stappen.recept_id = recept.id WHERE recept.id = '"+str(gid)+"'")
    mycursor.execute("SELECT recept.naam AS naam, stappen.StapBeschrijving AS Stapbeschrijving, stappen.volgorde AS volgorde , ingredient.naam AS inaam, ingredient.volgorde AS ivolgorde, ingredient.hoeveelheid AS ihoeveelheid FROM recept LEFT JOIN stappen ON stappen.recept_id = recept.id LEFT JOIN ingredient ON ingredient.recept_id = recept.id WHERE recept.id = '"+str(gid)+"'")
    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

def recepttoevoegen2temp(recept):
    mydb = algemenefuncties.verbindingdb()
    mycursor = mydb.cursor()
    sql = "INSERT INTO recept (naam, beschrijving, bereidingstijd) VALUES (%s, %s, %s)"
    val = (recept["naam"], recept["description"], recept["difficulty"])
    mycursor.execute(sql, val)
    mydb.commit()
    return str(mycursor.lastrowid)

def staptoevoegenaanrecept(stap, receptid):
    mydb = algemenefuncties.verbindingdb()
    mycursor = mydb.cursor()
    sql = "INSERT INTO stappen (Stapbeschrijving, volgorde, recept_id) VALUES (%s, %s, %s)"
    val = (stap["Stapbeschrijving"], stap["volgorde"], receptid)
    mycursor.execute(sql, val)
    mydb.commit()
    return "stap toevoegen"
