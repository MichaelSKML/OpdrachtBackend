import mysql.connector
import algemenefuncties

mydb = algemenefuncties.verbindingdb()

def receptdetails(gid):

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM recept WHERE id = " +str(gid))

  myresult = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  data = [
        dict(zip(keys, row)) for row in myresult
    ]
  return data

def ingredientbijrecept(gid):

  mycursor = mydb.cursor()

  mycursor.execute("SELECT ingredient.id, ingredient.hoeveelheid, ingredient.naam, ingredient.recept_id, recept.id FROM ingredient INNER JOIN recept ON ingredient.recept_id = recept.recept_id WHERE recept.id = " +str(gid))

  myresultingredient = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  dataingredient = [
        dict(zip(keys, row)) for row in myresultingredient
    ]
  return dataingredient

def stappenbijrecept(gid):
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT stappen.id, Stapbeschrijving, stappen.Afbeelding, stappen.recept_id, volgorde FROM stappen INNER JOIN recept ON stappen.recept_id = recept.recept_id WHERE recept.id = " +str(gid))

  myresultstappen = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  datastappen = [
        dict(zip(keys, row)) for row in myresultstappen
    ]
  return datastappen

def tagsbijrecept(gid):
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT idtag_recept, tag_id, naamtag FROM tag_recept INNER JOIN tag ON tag_id = idtag WHERE idtag_recept = " +str(gid))

  myresulttags = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  datatags = [
        dict(zip(keys, row)) for row in myresulttags
    ]
  return datatags

def reviewbijrecept(gid):
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT idreview, review.recept_id, gebruikersnaam, review, beoordeling FROM review INNER JOIN recept ON review.recept_id = recept.recept_id WHERE recept.id = " +str(gid))

  myresultreview = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  datareview = [
        dict(zip(keys, row)) for row in myresultreview
    ]
  return datareview

def receptdetailsgefilterd():
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT idtag_recept, tag_id, naamtag, recept.naam, recept.aantalsterren, recept.afbeelding FROM tag_recept INNER JOIN tag ON tag_id = idtag INNER JOIN recept ON recept.id = idtag_recept ORDER by naamtag;")

  myresultgefilderd = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]

  datagefilterd = [
        dict(zip(keys, row)) for row in myresultgefilderd
    ]
  return datagefilterd