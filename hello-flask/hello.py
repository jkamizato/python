from flask import Flask

import random

random_number = random.randint(0, 9)
print(f"Random number: {random_number}")

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def make_under(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper

@app.route('/')
@make_bold
@make_under
def hello_world():
    return 'Hello, World!'

@app.route('/number')
def number():
    return f"{random_number}"

if __name__ == "__main__":
    app.run(debug=True)