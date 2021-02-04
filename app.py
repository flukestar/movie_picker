from flask import Flask, redirect, render_template, request

import imdbscrapper

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/moviepicker")
def moviepicker():
    rank, title, year, poster = imdbscrapper.pick_movie()
    return render_template(
        "moviepicker.html", film=title, rank=rank, year=year, poster=poster
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect("/user/" + user)
    else:
        return render_template("login.html")
