from flask import Flask, render_template

# This project makes use of https://html5up.net/forty
# Project completed in under 5 mins, illustrating how easy it
# is to create a stunning responsive website with a template
# static/images - need to replace these generic images with actuals
# Use of chrome dev tools to style on the fly.
# 'document.body.contentEditable=true;' is a great way to edit


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)