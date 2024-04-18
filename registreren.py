from flask import Flask, request, session, render_template, redirect, url_for, jsonify
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__)
app.secret_key = "607aeae2805bbcc94ab67a45cc0dbbe797b27bb760a8afdf"  
app.config['SESSION_COOKIE_SAMESITE'] = 'None' 
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = True
from flask_session import Session
CORS(app)

Session(app)

mydb = mysql.connector.connect(
    host="yc2403allpurpose.mysql.database.azure.com",
    user="yc2403admin",
    password="abcd1234ABCD!@#$",
    database="demopythondag"
)

@app.route('/registreren', methods=['POST'])
def registreren_function():
    try:
        data = request.json   
        cursor = mydb.cursor()

        gebruikersnaam = data.get('gebruikersnaam')
        wachtwoord = data.get('wachtwoord')
        emailadres = data.get('emailadres')
        geboortedatum = data.get('geboortedatum')
        geslacht = data.get('geslacht')
        woonplaats = data.get('woonplaats')

        query = "INSERT INTO account (gebruikersnaam, wachtwoord, emailadres, geboortedatum, geslacht, woonplaats) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (gebruikersnaam, wachtwoord, emailadres, geboortedatum, geslacht, woonplaats))
        
        mydb.commit()
        
        cursor.close()
        mydb.close()

        return jsonify({"message": "Account succesvol aangemaakt!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "Er is een fout opgetreden."}), 500
        
@app.route('/')
def login_form():
    return render_template('inloggen.html')

@app.route('/login', methods=['POST'])
def login():
    data_json = json.loads(request.data.decode('utf-8'))
    username = data_json["gebruikersnaam"]
    password = data_json["wachtwoord"]
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM account WHERE gebruikersnaam = %s AND wachtwoord = %s", (username, password))
    user = cursor.fetchone()

    if user:
        session['loggedin'] = True
        session['gebruikersnaam'] = user[1] 
        mijndata = list(user)
        mijndata[4] = mijndata[4].isoformat()
        data = tuple(mijndata)
        return json.dumps(data), 201
    else:
        return "Het inloggen is niet gelukt!", 401

def check_email_exists(email):
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM account WHERE emailadres = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        
        return user is not None
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

if __name__ == '__main__':
    app.run(debug=True)