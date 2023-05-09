from flask import Blueprint, request, jsonify
import sqlite3


# Define a new Blueprint
api = Blueprint("api", __name__)

#########################
# LIST TAGS
@api.get("/api/tags")
def list_tags():
    return

#########################
# LIST TODOS
@api.get("/api/todos")
def list_todos():

    # Connect to the database and execute the query
    conn = sqlite3.connect("veasTagEndringer.sqlite3")

    cursor_count_total = conn.cursor()
    cursor_count_total.execute("SELECT count(Todo_ID) FROM todos")
    count_total = cursor_count_total.fetchone()[0]

    cursor_count_filtered = conn.cursor()
    cursor_count_filtered.execute("SELECT count(Todo_ID) FROM todos WHERE TodoName = 'merit'")
    count_filtered = cursor_count_filtered.fetchone()[0]

    cursor_data = conn.cursor()
    cursor_data.execute("SELECT * FROM todos WHERE TodoName = 'merit' LIMIT 1")

    # Get the column names and rows from the query results
    columns = [column[0] for column in cursor_data.description]
    # rows = [row for row in cursor.fetchall()]
    rows = [dict(zip(columns,row)) for row in cursor_data.fetchall()]

    # Close the database connection
    conn.close()

    return {
        "meta": {
            "count_total": count_total,
            "count_filtered": count_filtered
        },
        "data": rows
    }

#########################
# GET TAG BY ID
@api.get("/api/tags/<id>")
def get_tag_by_id(id):
    print(f"id: {id}")
    return f"return id{id}"

#########################
# GET TODO BY ID
@api.get("/api/todos/<id>")
def get_todo_by_id(id):
    print(f"id: {id}")
    return f"return id{id}"

#########################
# CREATE TAG
@api.post("/api/tags")
def create_tag():
    return

#########################
# CREATE TODO
@api.post("/api/todos")
def create_todos():
    return

#########################
# UPDATE TAG
@api.patch("/api/tags/<id>")
def update_tag(id):
    print(f"id: {id}")
    return f"return id{id}"

#########################
# UPDATE TODO
@api.patch("/api/todos/<id>")
def update_todo(id):
    print(f"id: {id}")
    return f"return id{id}"

#########################
# DELETE TAG
@api.delete("/api/tags/<id>")
def delete_tag(id):
    print(f"id: {id}")
    return f"return id{id}"

#########################
# DELETE TODO
@api.delete("/api/todos/<id>")
def delete_todo(id):
    print(f"id: {id}")
    return f"return id{id}"



