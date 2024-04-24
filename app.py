# pip install flask
# pip install flask-cors
# pip install Flask-Session

from flask import Flask
from flask_cors import CORS
import json
import requests
from flask import Flask, request, session, render_template, redirect, url_for, jsonify

import erik
import felix
import dominique
import registreren
import michael

app = Flask(__name__)
app.secret_key = "607aeae2805bbcc94ab67a45cc0dbbe797b27bb760a8afdf"  
app.config['SESSION_COOKIE_SAMESITE'] = 'None' 
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = True
from flask_session import Session
CORS(app)

Session(app)

@app.route("/")
def helloWorld():
  return "Onze web app is nu online!"

@app.route("/felix")
def methodefelix():
  return felix.methodevanfelix()

@app.route("/felix2")
def methodefelix2():
  return felix.tweedemethodevanfelix()

@app.route("/felix3/<variabele1>")
def methodefelix3(variabele1):
  return felix.derdemethodevanfelix(variabele1)

@app.route("/dominique")
def methodedominique():
    return dominique.open_youtube_link('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route("/erik/<eenword>/<tweeword>")
def methodeerik(eenword, tweeword):
  return erik.methodeerik(eenword, tweeword)


@app.route("/felixjson")
def felixjson():
  return felix.nuechtmetjson()

@app.route("/felixpost", methods=['POST'])
def felixpost():
  data_json = json.loads(request.data.decode('utf-8'))
  print(data_json["naam"])
  return "hoi"

@app.route("/registreren", methods=['POST'])
def registreren_route():
    return registreren.registreren_function()

@app.route('/login', methods=['POST', 'GET'])
def inloggen_route2():
    if request.method == 'POST':
        return registreren.login()
        # return "test3232232"
    else:
        # Render the login form from the templates folder
        return render_template('login.html')
  
@app.route('/checkemail', methods=['POST'])
def check_email_route():
    data = request.json
    email = data.get('email')
    
    exists = registreren.check_email_exists(email)
    
    return jsonify({"exists": exists}), 200
  
@app.route('/accountpagina/<username>')
def account_route(username):
    return registreren.account_route(username)

@app.route('/receptdetails/<gid>')
def detailsrecept(gid):
    varreceptdetails = michael.receptdetails(gid)
    varingredientbijrecept = michael.ingredientbijrecept(gid)
    varstappen = michael.stappenbijrecept(gid)
    vartags = michael.tagsbijrecept(gid)
    varreviews = michael.reviewbijrecept(gid)
    return {"recept": varreceptdetails[0] , "ingredient": varingredientbijrecept, "stappen": varstappen, "tags": vartags, "review": varreviews}

@app.route('/receptaanmaken/<stap>')
def staptoevoegen(stap):
    return erik.staptoevoegen(stap)

@app.route('/receptaanmaken/<naam>')
def receptnaamtoevoegen(naam):
    return erik.receptnaamtoevoegen(naam)

@app.route('/receptdetails2temp/<gid>')
def recept2tempdetails(gid):
  return felix.receptdetailsvanrecept(gid)

@app.route('/recepttevoegen2temp', methods=['POST'])
def recepttoevoegen2temp():
  data_json = json.loads(request.data.decode('utf-8'))
  return felix.recepttoevoegen2temp(data_json)

@app.route('/staptoevoegenaanrecept/<receptid>', methods=['POST'])
def staptoevoegenaanrecept(receptid):
  data_json = json.loads(request.data.decode('utf-8'))
  return felix.staptoevoegenaanrecept(data_json, receptid)

@app.route('/ingredienttoevoegenaanrecept/<receptid>', methods=['POST'])
def ingredienttoevoegenaanrecept(receptid):
  data_json = json.loads(request.data.decode('utf-8'))
  return erik.ingredienttoevoegenaanrecept(data_json, receptid)

@app.route('/tagtoevoegen/<receptid>', methods=['POST'])
def tagtoevoegen(receptid):
  data_json = json.loads(request.data.decode('utf-8'))
  return erik.tagtoevoegen(data_json, receptid)

@app.route('/email', methods=['POST'])
def email():
    try:
        emailadres = request.json.get('emailadres')
        
        exists = registreren.check_email_exists(emailadres)
        
        if exists:
            return jsonify({"message": ""}), 200
        else:
            return jsonify({"message": ""}), 404

    except KeyError:
        return jsonify({"message": "Emailadres is niet ingevuld!"}), 400
    
  @app.route("/mike")
def methodemike():
  return felix.methodevanmike()