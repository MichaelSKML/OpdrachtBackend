from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import json
import os
from dotenv import load_dotenv

# Flask app initialisatie en CORS aanzetten
app = Flask(__name__)
CORS(app)

# Database connectie
load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Endpoint voor het registreren van een nieuwe gebruiker
@app.route('/registreren', methods=['POST'])
def registreren_function():
    try:
        # JSON data uit het request halen en database cursor activeren
        data = request.json   
        cursor = mydb.cursor()

        # Gebruikersdata uit het request halen
        gebruikersnaam = data.get('gebruikersnaam')
        wachtwoord = data.get('wachtwoord')
        emailadres = data.get('emailadres')
        geboortedatum = data.get('geboortedatum')
        geslacht = data.get('geslacht')
        woonplaats = data.get('woonplaats')

        # SQLquery voor het invoegen van een nieuwe gebruiker
        query = "INSERT INTO account (gebruikersnaam, wachtwoord, emailadres, geboortedatum, geslacht, woonplaats) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (gebruikersnaam, wachtwoord, emailadres, geboortedatum, geslacht, woonplaats))
        
        # Wijzigingen in de database opslaan en database cursor sluiten
        mydb.commit()
        cursor.close()

        # Succelvol aangemaakt terugsturen
        return jsonify({"message": "Account succesvol aangemaakt!"}), 200

    # Foutmelding en statuscode bij een fout
    except Exception as e:
        print(e)
        return jsonify({"message": "Er is een fout opgetreden."}), 500


# Endpoint voor het inloggen van een gebruiker
@app.route('/login', methods=['POST'])
def login():
    # JSON data uit het request halen en database cursor activeren
    data_json = json.loads(request.data)
    username = data_json["gebruikersnaam"]
    password = data_json["wachtwoord"]
    
    cursor = mydb.cursor()
    # SQLquery voor het selecteren van een gebruiker op basis van gebruikersnaam en wachtwoord en vervolgens de database cursor sluiten.
    cursor.execute("SELECT * FROM account WHERE gebruikersnaam = %s AND wachtwoord = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()

    # Gebruikersinformatie aanpassen voor de frontend
    if user:
        mijndata = list(user)                       # Maak lijst van userdata.
        mijndata[2] = ""                            # 2 = Wachtwoord verwijderen (empty string).
        mijndata[4] = mijndata[4].isoformat()       # 4 = Datum omzetten naar ISO-formaat (ivm verwerken database format).
        data = tuple(mijndata)                      # Bovenstaande lijst terugzetten naar een tuple.
        return json.dumps(data), 201                # Data tuple word omgezet naar JSON string met een 201 statuscode. 
    else:
        # Foutmelding en 401 statuscode bij mislukte login
        return "Het inloggen is niet gelukt!", 401

# Functie om te controleren of een e-mailadres al bestaat in DB
def check_email_exists(email):
    try:
        cursor = mydb.cursor()
        # SQLquery voor het selecteren van een gebruiker op basis van e-mailadres en vervolgens de database cursor sluiten.
        cursor.execute("SELECT * FROM account WHERE emailadres = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        
        # True als e-mailadres al bestaat, anders False
        return user is not None
    
    # Foutmelding en False bij een fout
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Flask app starten
if __name__ == '__main__':
    app.run(debug=True)