from flask import Flask, render_template, redirect, request

App = Flask(__name__)


@App.route('/')
def hello():
    return render_template('index.html')


@App.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "hello"
    else:
        render_template('auth/login.html')


if __name__ == "__main__":
    App.run(debug=True)
