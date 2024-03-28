from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# Database Config 
mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com", 
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

@app.route('/accountaanmaken')
def registreren():
    gebruikersnaam = request.form['gebruikersnaam']
    email = request.form['email']
    wachtwoord = request.form['wachtwoord']
    geboortedatum = request.form['geboortedatum']
    geslacht = request.form['geslacht']
    woonplaats = request.form['woonplaats']

    try:
        # Verbinden met de database
        mydb = mysql.connector.connect(**mydb)
        cursor = mydb.cursor() 
        # Voeg nieuwe gebruiker toe in database
        cursor.execute("INSERT INTO gebruikers (gebruikersnaam, email, wachtwoord, geboortedatum, geslacht, woonplaats) VALUES (%s, %s, %s, %s, %s, %s)", (gebruikersnaam, email, wachtwoord, geboortedatum, geslacht, woonplaats))
        mydb.commit()

        return 'Account succesvol aangemaakt!'
    except mysql.connector.Error as e:
        return str(e)
    finally:
        cursor.close()
        mydb.close()

if __name__ == '__main__':
    app.run(debug=True)
