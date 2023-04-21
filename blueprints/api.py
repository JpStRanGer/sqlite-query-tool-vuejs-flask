from flask import Blueprint, request, jsonify
import sqlite3

# Define a new Blueprint
api = Blueprint("example", __name__)


# DEMO FOR TESTING BL (Blueprints)
@api.route("/bl")
def index():
    return "Hello, World! From your Blueprint!"


# Select all colloums from User
@api.route("/query", methods=["GET","post"])
def query():
    # Get the query from the request body
    query = request.json["query"]
    
    return sqlQuery(query)
    return jsonify({"columns": ("column1","column2","column3"), "rows": ["row1","row2","row3"]})
    return query


# functions
def sqlQuery(query):
    print("sqlQuery")
    # Connect to the database and execute the query
    # conn = sqlite3.connect("test.db")
    conn = sqlite3.connect("veasTagEndringer.sqlite3")
    cursor = conn.cursor()
    cursor.execute(query)

    # Get the column names and rows from the query results
    columns = [column[0] for column in cursor.description]
    rows = [row for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    # Return the query results as JSON
    return jsonify({"columns": columns, "rows": rows})

# Select all colloums from User
@api.route("/testquery", methods=["GET","post"])
def testquery():
    print("/testquery")
    # Get the query from the request body
    query = request.json["query"]
    
    print("sqlQuery")
    # Connect to the database and execute the query
    # conn = sqlite3.connect("test.db")
    conn = sqlite3.connect("veasTagEndringer.sqlite3")
    cursor = conn.cursor()
    cursor.execute(query)

    # Get the column names and rows from the query results
    columns = [column[0] for column in cursor.description]
    rows = [row for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    # Return the query results as JSON
    return jsonify({"columns": columns, "rows": rows})

