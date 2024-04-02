from flask import Flask, request, session, render_template, redirect, url_for
from flask_cors import CORS
import mysql.connector

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
    gebruikersnaam = request.form['gebruikersnaam']
    wachtwoord = request.form['wachtwoord']
    email = request.form['email']
    geboortedatum = request.form['geboortedatum']
    geslacht = request.form['geslacht']
    woonplaats = request.form['woonplaats']

    print("Received Form Data:")
    print(f"Gebruikersnaam: {gebruikersnaam}")
    print(f"Email: {email}")
    print(f"Wachtwoord: {wachtwoord}")
    print(f"Geboortedatum: {geboortedatum}")
    print(f"Geslacht: {geslacht}")
    print(f"Woonplaats: {woonplaats}")

    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO gebruikers2 (gebruikersnaam, email, wachtwoord, geboortedatum, geslacht, woonplaats) VALUES (%s, %s, %s, %s, %s, %s)", (gebruikersnaam, email, wachtwoord, geboortedatum, geslacht, woonplaats))
        mydb.commit()
        cursor.close()  

        return """
        <script>
        setTimeout(function() {
            window.location.href = 'http://127.0.0.1:5500/accountpagina.html';
        }, 9000);
        </script>
        Account succesvol aangemaakt!
        """

    except mysql.connector.Error as e:
        print("Oeps! Er ging iets mis.", e)
        return str(e)
        
@app.route('/')
def login_form():
    return render_template('inloggen.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['gebruikersnaam']
    password = request.form['wachtwoord']

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM gebruikers2 WHERE gebruikersnaam = %s AND wachtwoord = %s", (username, password))
    user2 = cursor.fetchone()

    if user2:
        session['loggedin'] = True
        session['gebruikersnaam'] = user2[1]
        session['wachtwoord'] = user2[2]
        session['email'] = user2[3]
        session['geboortedatum'] = user2[4]
        session['geslacht'] = user2[5]
        session['woonplaats'] = user2[6]

        return """
        <script>
        setTimeout(function() {
            window.location.href = 'http://127.0.0.1:5500/accountpagina.html';
        }, 2000);
        </script>
        Je bent nu ingelogd!
        """
    else:
        return "Het inloggen is niet gelukt."

@app.route('/email', methods=['POST'])
def email():
    emailadres = request.form['email']
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM gebruikers2 WHERE email = %s" (emailadres))
    user3 = cursor.fetchone()
    
    if user3:
        return "Email verzonden!"
    else:
        return "Email niet gevonden!"

@app.route('/accountpagina')
def account_route():
    if 'loggedin' in session:
        return render_template('accountpagina.html', 
                               gebruikersnaam=session.get('gebruikersnaam'), 
                               wachtwoord=session.get('wachtwoord'), 
                               email=session.get('email'), 
                               geboortedatum=session.get('geboortedatum'), 
                               geslacht=session.get('geslacht'), 
                               woonplaats=session.get('woonplaats'))
    else:
        return redirect(url_for('login_form')) 
    
if __name__ == '__main__':
    app.run(debug=True)