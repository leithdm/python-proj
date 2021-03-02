from flask import Flask, render_template
import requests
from post import Post

URL = "https://api.npoint.io/6641855599166a4e5de3"
all_posts = requests.get(url=URL).json()
all_posts_list = []
for item in all_posts:
    post = Post(item['id'], item['title'], item['subtitle'], item['body'])
    all_posts_list.append(post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts_list)


@app.route('/post/<int:id>')
def get_post(id):
    post = all_posts_list[id - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
