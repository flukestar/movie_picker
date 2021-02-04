from flask import Flask, redirect, render_template, request

import imdbscrapper

app = Flask(__name__)


@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/moviepicker")
def moviepicker():
    title = "Movie Picker"
    rank, film, year, poster = imdbscrapper.pick_movie()
    return render_template(
        "moviepicker.html", film=film, rank=rank, year=year, poster=poster, title=title
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    title = "Login"
    if request.method == "POST":
        user = request.form["nm"]
        return redirect("/user/" + user)
    else:
        return render_template("login.html", title=title)
