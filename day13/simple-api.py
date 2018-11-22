from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# TODO: Store our heroes in a database
heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace', "lovely": True}, {'person': 'Guido_van_Rossum'}]

@app.route("/api/heroes", methods=["GET"])
def all_heroes():
    return jsonify({"heroes": heroes})

# localhost:5000/api/heroes/Peter_Norvig
@app.route("/api/heroes/<string:name>", methods=["GET"])
def single_hero(name):
    # You may need to ponder this line: list comprehensions!
    particular_heroes = [ hero for hero in heroes if hero["person"] == name ]
    if particular_heroes:
        particular_hero = particular_heroes[0] # Extract the dictionary from the list.
        return jsonify(particular_hero)
    else:
        return jsonify({"error": "Hero not found"})

@app.route("/api/heroes", methods=["POST"])
def add_hero():
    new_hero = {"person": request.form["person"]}
    heroes.append(new_hero)
    # TODO: inspect request data to see if we should return JSON or HTML
    return jsonify({"heroes": heroes})

# Our first/only HTML page for this application
@app.route("/heroes/add")
def add_hero_form():
    return render_template("heroes_add.html")

if __name__ == "__main__":
    app.run(debug=True)
