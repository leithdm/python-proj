from flask import Flask, render_template
import requests
import datetime

posts = requests.get("https://api.npoint.io/6641855599166a4e5de3").json()
current_year = datetime.datetime.now().year

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts, year=current_year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


@app.route("/about")
def about():
    return render_template("about.html", year=current_year)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
