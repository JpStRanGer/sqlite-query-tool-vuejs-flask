from flask import Flask, render_template, jsonify, request
from blueprints.testing import testing
from blueprints.api import api
import sqlalchemy
import sqlite3
# import requests

app = Flask(__name__)
# BLUEPRINT REGISTRATION
app.register_blueprint(testing)
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2')
def index2():
    return render_template('index2.html')


#  
# SQL TESTING!!!!!
#  




@app.route('/get', methods=["GET","post"])
def sqlSelect():
    args = request.args
    try:
        # CONNECTING TO DB
        # conn = sqlite3.connect("test.db")
        conn = sqlite3.connect("veasTagEndringer.sqlite3")

        cur = conn.cursor()
        cur.execute("Select * from TagHistory")
        result = cur.fetchall()
    except:
        return "error - could not connect to DB!"

    return request.get_data()
    return jsonify(request.args, request.get_data())
    return jsonify("GET OK!", request.args, {"queryResult":result})
    return jsonify("GET OK!")


if __name__ == '__main__':
    app.run( debug = True)
