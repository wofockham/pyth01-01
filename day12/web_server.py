from flask import Flask, render_template
import os
import random

import secrets
import rumours

app = Flask(__name__)

my_job_title =  "Python professional"

file_path = '.' # Current directory
with open(os.path.join(file_path, 'sonnet.txt')) as f:
    the_text = f.read()

@app.route('/')
def index():
    # return render_template('index.html')
    # return "Hello, my job title is " + my_job_title
    # return "Hello " + secrets.username + ", the password is: " + secrets.password
    # return "Here is a fun fact about the royals: " + rumours.royals
    return the_text

@app.route('/sayHi')
def say_hi():
    return "Hello!"

@app.route('/dice')
def dice():
    value = random.randint(1, 6)
    return str(value) # Web servers always output strings

@app.route('/dice/<sides>')
def roll(sides):
    value = random.randint(1, int(sides))
    return str(value)

@app.route('/family/<name>')
def hello(name):
    return "Hello, " + name

@app.route('/repeat/<input>')
def repeat(input):
    # return input + input + input + input
    return input * 4

if __name__ == "__main__":
    app.run(debug=True)
