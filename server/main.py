from flask import Flask

# Init with Flask minimal project starter.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"