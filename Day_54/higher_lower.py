from flask import Flask
import random

app = Flask(__name__)

my_guess = random.choice(range(0,10))

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def check(number):
    if number > my_guess:
        return "<h3 style='color:blue'>Too high</h3>\
            <img src='https://media.giphy.com/media/s5CJw8UPITK6I/giphy.gif'>"
    elif number < my_guess:
        return "<h3 style='color:red'>Too low</h3>\
            <img src='https://media.giphy.com/media/2sfEg0Yv4c8E5VT7s3/giphy.gif'>"
    else:
        return "<h2 style='color:green'> You Guessed correct</h2>\
            <img src='https://media.giphy.com/media/JKcneNkriqxQbE8e49/giphy.gif'>"




if __name__ == "__main__":
    app.run(debug=True)