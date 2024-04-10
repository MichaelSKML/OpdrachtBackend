import mysql.connector

def receptdetails(gid):
  
  mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM recept WHERE id = " +str(gid))

  myresult = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  data = [
        dict(zip(keys, row)) for row in myresult
    ]
  return data

def ingredientbijrecept(gid):
  
  mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT ingredient.id, ingredient.naam, ingredient.recept_id, recept.id FROM ingredient INNER JOIN recept ON ingredient.recept_id = recept.recept_id WHERE recept.id = " +str(gid))

  myresultingredient = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  dataingredient = [
        dict(zip(keys, row)) for row in myresultingredient
    ]
  return dataingredient
