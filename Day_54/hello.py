from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def make_bold(function):
    def make():
        return "<b>function</b>"
    return make


def make_emphasis(function):
    def emp():
        return "<em>function</em>"
    return emp

def make_underline(function):
    def under():
        return "<u>function</u>"
    return under


@app.route("/login")
@make_bold
@make_emphasis
@make_underline
def login():
    return "Login Page"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)