from flask import Flask, render_template
import os

app = Flask(__name__)

file_path = "."
with open(os.path.join(file_path, 'sonnet.txt')) as f:
    sonnet = f.read()

@app.route("/")
def index():
    return render_template("hello.html", poem=sonnet)

if __name__ == "__main__":
    app.run(debug=True)
