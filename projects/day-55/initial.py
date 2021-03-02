from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        function()
    return wrapper_function


# diff routes using app.route decorator
@app.route("/")
@make_bold
def index():
    return 'Hello'

# using in-line styling
@app.route("/style")
def style():
    return '<h1 style="text-align: center">Style Page</h1><p>lorem lorem lorem</p>' \
           '<img src="https://media.giphy.com/media/4Z3DdOZRTcXPa/giphy.gif">'

# creating variable paths and converting path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"


if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)


