from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', year = current_year)


@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    gender = guess_gender(name)
    age = guess_age(name)
    return render_template('guess.html', name = name, gender = gender, age = age)

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blogs = response.json()
    return render_template('blog.html', blogs = blogs)


def guess_gender(usr_name):
    response = requests.get(f'https://api.genderize.io/?name={usr_name}')
    if response.status_code == 200:
        gender = response.json()['gender']
        return gender
    else:
        return 'Gender not found'

def guess_age(usr_name):
    response = requests.get(f'https://api.agify.io/?name={usr_name}')
    if response.status_code == 200:
        age = response.json()['age']
        return age
    else:
        return 'Gender not found'
  

if __name__ == '__main__':
    app.run(debug=True)