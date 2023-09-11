"""
Flask is open source web development framework that allows us to build lightweight web applications quickle and easily with Flask Libraries.
"""
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/feature')
def feature():
    return render_template("feature.html")

@app.route('/support')
def support():
    return render_template("support.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")


if __name__=="__main__":
    app.run(debug=True)
