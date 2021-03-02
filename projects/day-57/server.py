from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1, 10)
    # setup copyright year to always be correct...
    year = datetime.datetime.now().year
    return render_template("starter_index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def get_age(name):
    URL = f"https://api.agify.io?name={name}"
    parameters = {
        "name": {name}
    }

    response = requests.get(url=URL)
    response.raise_for_status()
    date = response.json()
    age = date["age"]
    return render_template("age.html", name=name, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    URL = "https://api.npoint.io/6641855599166a4e5de3"
    response = requests.get(url=URL)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

