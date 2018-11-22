from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", greeting="HELLO WORLD")

@app.route("/goodbye")
def goodbye():
    return render_template("index.html", greeting="GOODBYE WORLD")

@app.route("/dice/<int:sides>") # Automatic type conversion
def roll(sides):
    result = random.randint(1, sides)
    message = "You rolled a " + str(result)
    return render_template("index.html", greeting=message)

if __name__ == "__main__":
    app.run(debug=True)
