# pip install flask
# pip install flask-cors
# pip install Flask-Session

from flask import Flask
from flask_cors import CORS
import json
import requests
from flask import Flask, request, session, render_template, redirect, url_for

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

@app.route('/login', methods=['POST'])
def inloggen_route2():
    return registreren.login()
  
@app.route('/email', methods=['POST'])
def email_route():
    return registreren.email()
  
@app.route('/accountpagina')
def account_route():
    return registreren.account_route()

@app.route('/receptdetails/<gid>')
def detailsrecept(gid):
    varreceptdetails = michael.receptdetails(gid)
    varingredientbijrecept = michael.ingredientbijrecept(gid)
    varstappen = michael.stappenbijrecept(gid)
    return {"recept": varreceptdetails[0] , "ingredient": varingredientbijrecept, "stappen": varstappen}

@app.route('/receptaanmaken/<stap>')
def staptoevoegen(stap):
    return erik.staptoevoegen(stap)

@app.route('/receptaanmaken/<naam>')
def receptnaamtoevoegen(naam):
    return erik.receptnaamtoevoegen(naam)
