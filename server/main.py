from flask import Flask

# Init with Flask minimal project starter.
app = Flask(__name__)

@app.route("/")
def get_fastest_normal():
    return "<p>Hello, World!</p>"