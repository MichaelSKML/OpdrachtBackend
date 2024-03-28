

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

def methodeerik2():
    mydb = onzepython.mydb

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM recept")

    myresult = mycursor.fetchall()
    eindstring = ""
    for x in myresult:
        print(x[1], " - ", x[3])
        eindstring += x[1]+", "
    return "yes: " + eindstring

