from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    return "Login Page"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)