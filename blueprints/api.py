from flask import Blueprint, request, jsonify
import sqlite3


# Define a new Blueprint
api = Blueprint("example", __name__)


##################################
# DEMO FOR TESTING BL (Blueprints)
@api.route("/bl")
def index():
    print(f"request.method: {request.method}")
    print(f"request.data: {request.data}")
    print(f"request.args: {request.args}")
    return "Hello, World! From your Blueprint!"


##################################
# Select all colloums from User
@api.route("/query", methods=["GET","post"])
def query():
    print()
    print("query()")
    # Get the query from the request body
    query = request.json["query"]
    
    return sqlQuery(query)


###########################
# functions
def sqlQuery(query):
    print("sqlQuery(query)")
    print(f"request.method: {request.method}")
    print(f"request.args(GET): {request.args}")
    print(f"request.data(POST): {request.data}")
    print()
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


################################
# Select all colloums from User
@api.route("/testquery", methods=["GET","post"])
def testquery():
    print("/testquery")
    if request.method == "get" or request.method == "post":
        # Get the query from the request body
        query = request.json["query"]
    else:
        query = "SELECT * FROM sqlite_master WHERE type='view' or type='table'"
    
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

