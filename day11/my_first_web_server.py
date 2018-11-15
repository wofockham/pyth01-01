from flask import Flask

app = Flask(__name__)

# Define a path: "/" is the root or index path.
@app.route('/')
def index():
    return 'Goodbye Cruel World!' # Whatever is returned will be the content of the page.

# This decorator connects the function to the route.
@app.route('/about')
def about():
    return 'This app is a work in progress'

# Only start the server if we've run this file from the command line (not via import)
if __name__ == "__main__":
    app.run(debug=True)
