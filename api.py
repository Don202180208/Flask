from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Astiggwapo12345"
app.config["MYSQL_DB"] = "sakila"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
auth = HTTPBasicAuth()

users = {"admin": "password"}


@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username


@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "Unauthorized access"}), 401)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/actors", methods=["GET"])
@auth.login_required
def get_actors():
    data = data_fetch("""select * from actor""")
    return make_response(jsonify(data), 200)


@app.route("/actors/<int:id>", methods=["GET"])
def get_actor_by_id(id):
    data = data_fetch("""SELECT * FROM actor where actor_id = {}""".format(id))
    return make_response(jsonify(data), 200)


@app.route("/actors/<int:id>/movies", methods=["GET"])
def get_movies_by_actor(id):
    data = data_fetch(
        """
        SELECT film.title, film.release_year 
        FROM actor 
        INNER JOIN film_actor
        ON actor.actor_id = film_actor.actor_id 
        INNER JOIN film
        ON film_actor.film_id = film.film_id 
        WHERE actor.actor_id = {}
    """.format(
            id
        )
    )
    return make_response(
        jsonify({"actor_id": id, "count": len(data), "movies": data}), 200
    )


@app.route("/actors", methods=["POST"])
def add_actor():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    cur.execute(
        """ INSERT INTO actor (first_name, last_name) VALUE (%s, %s)""",
        (first_name, last_name),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


@app.route("/actors/<int:id>", methods=["PUT"])
def update_actor(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    cur.execute(
        """ UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s """,
        (first_name, last_name, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/actors/<int:id>", methods=["DELETE"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM actor where actor_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/actors/search", methods=["POST"])
def search_actors():
    search_criteria = request.get_json()
    first_name = search_criteria.get("first_name")
    last_name = search_criteria.get("last_name")
    # Modify the query to include the search criteria
    query = f"""
        SELECT * 
        FROM actor 
        WHERE first_name LIKE '{first_name}%' AND last_name LIKE '{last_name}%'
    """
    data = data_fetch(query)
    return make_response(jsonify(data), 200)


@app.route("/actors/format", methods=["GET"])
def get_params():
    fmt = request.args.get("id")
    foo = request.args.get("aaaa")
    return make_response(jsonify({"format": fmt, "foo": foo}), 200)


if __name__ == "__main__":
    app.run(debug=True)
