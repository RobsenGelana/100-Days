from flask import Flask, render_template
import requests
import random
import datetime

GENDER_URL = "https://api.genderize.io"
AGE_URL = "https://api.agify.io"
app = Flask(__name__)


@app.route("/")
def home_page():
    current_date = datetime.date.today().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, cur_date=current_date)

@app.route("/guess/<name>")
def guess(name):
    params = {
        'name': name
    }
    response_age = requests.get(AGE_URL, params=params)
    ages = response_age.json()
    age = ages['age']
    response_gender = requests.get(GENDER_URL, params=params)
    genders = response_gender.json()
    gender = genders['gender']
    return render_template('guess.html', ag=age, gn=gender, na=name)

if __name__ == "__main__":
    app.run(debug=True)