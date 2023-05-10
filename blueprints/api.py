from flask import Blueprint, request, jsonify
import sqlite3

# functions
def generate_query_variables(search_columns: dict = {}) -> list:

    # search for first matching query argument key
    search_column = None
    for key in search_columns:
        if key in request.args:
            search_column = key
            break

    # build where clause
    query_where = ""
    query_values = ()
    if search_column is not None:
        # query_where = "WHERE TodoName = 'merit'"
        query_where = f"WHERE {search_columns[search_column]} = ?"
        query_values += (request.args[search_column],)

    # get amount of rows/results per page
    per_page = 100
    if "per_page" in request.args:
        per_page = int(request.args["per_page"])
    if per_page < 0 or per_page > 5000:
        per_page = 100

    # get page number
    page = 1
    if "page" in request.args:
        page = int(request.args["page"])
    if page < 1:
        page = 1

    # build offset,limit clause
    offset = (page - 1) * per_page
    query_limit = f"LIMIT {offset},{per_page}"

    return query_where, query_values, query_limit


def get_result_for_list_endpoint(
    db_conn_name: str, table_name: str, id_column: str, search_columns: dict = {}
) -> dict:

    query_where, query_values, query_limit = generate_query_variables(search_columns)

    # Connect to the database and execute the query
    conn = sqlite3.connect(db_conn_name)

    cursor_count_total = conn.cursor()
    cursor_count_total.execute(f"SELECT count({id_column}) FROM {table_name}")
    count_total = cursor_count_total.fetchone()[0]

    cursor_count_filtered = conn.cursor()
    cursor_count_filtered.execute(
        f"SELECT count({id_column}) FROM {table_name} {query_where}", query_values
    )
    count_filtered = cursor_count_filtered.fetchone()[0]

    cursor_data = conn.cursor()
    cursor_data.execute(
        f"SELECT * FROM {table_name} {query_where} {query_limit}", query_values
    )

    # Get the column names and rows from the query results
    columns = [column[0] for column in cursor_data.description]
    rows = cursor_data.fetchall()
    rows = [dict(zip(columns, row)) for row in rows]

    # Close the database connection
    conn.close()

    return {
        "meta": {"count_total": count_total, "count_filtered": count_filtered},
        "data": rows,
    }


def get_result_for_id_endpoint(
    db_conn_name: str, table_name: str, id_column: str, id: int
) -> dict:

    # Connect to the database and execute the query
    conn = sqlite3.connect(db_conn_name)

    cursor_data = conn.cursor()
    cursor_data.execute(
        f"SELECT * FROM {table_name} WHERE {id_column} = ? LIMIT 1", (id,)
    )

    # Get the column names and rows from the query results
    columns = [column[0] for column in cursor_data.description]
    row = cursor_data.fetchone()
    if row is not None:
        row = dict(zip(columns, row))

    # Close the database connection
    conn.close()

    return {"meta": {}, "data": row}


# Define a new Blueprint
api = Blueprint("api", __name__)

#########################
# LIST TAGS
@api.get("/api/tags")
def list_tags():
    return get_result_for_list_endpoint(
        "veasTagEndringer.sqlite3", "TagsWithTodo", "Tag_ID"
    )


#########################
# LIST TODOS
@api.get("/api/todos")
def list_todos():
    return get_result_for_list_endpoint(
        "veasTagEndringer.sqlite3", "Todos", "Todo_ID", {"name": "TodoName"}
    )


#########################
# GET TAG BY ID
@api.get("/api/tags/<id>")
def get_tag_by_id(id):
    return get_result_for_id_endpoint(
        "veasTagEndringer.sqlite3", "TagsWithTodo", "Tag_ID", id
    )


#########################
# GET TODO BY ID
@api.get("/api/todos/<id>")
def get_todo_by_id(id):
    return get_result_for_id_endpoint(
        "veasTagEndringer.sqlite3", "Todos", "Todo_ID", id
    )


#########################
# CREATE TAG
@api.post("/api/tags")
def create_tag():

    conn = sqlite3.connect("veasTagEndringer.sqlite3")
    cursor = conn.cursor()

    # create new row in Tags table
    cursor.execute("INSERT INTO Tags (CreationDate) VALUES (datetime('now'));")
    # Get ID of new tag
    tag_id = cursor.lastrowid

    # Create new row in TagHistory table
    cursor.execute(
        "INSERT INTO TagHistory (Tag_ID, Name, Description, ChangeDate) VALUES (?,?,?,datetime('now'));",
        (
            tag_id,
            request.json["name"],
            request.json["description"],
        ),
    )
    conn.commit()
    conn.close()
    # Get data of new tag and return response
    return get_result_for_id_endpoint(
        "veasTagEndringer.sqlite3", "TagsWithTodo", "Tag_ID", tag_id
    )



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
