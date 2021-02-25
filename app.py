from datetime import datetime
from os import environ


from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


import imdbscrapper

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    environ.get("DATABASE_URL") or "sqlite:///mysite.db"
)
db = SQLAlchemy(app)

# Database Models for Watched Films
class Watched(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(200), nullable=False)
    watched_date = db.Column(db.DateTime, default=datetime.utcnow)
    picked_by = db.Column(db.String(200), nullable=False)
    poster = db.Column(
        db.String(800),
        default="https://m.media-amazon.com/images/S/sash/85lhIiFCmSScRzu.png",
    )

    def __repr__(self):
        return (
            "<Watched(movie='%s', watched_date='%r', picked_by='%s', poster='%s')>"
            % (
                self.movie,
                self.watched_date,
                self.picked_by,
                self.poster,
            )
        )


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


@app.route("/seen")
def seen():
    title = "Seen"
    film_lists = Watched.query.order_by(Watched.watched_date.desc())
    return render_template("watched.html", title=title, film_lists=film_lists)


@app.route("/scores")
def scores():
    title = "Scores"
    return render_template("scores.html", title=title)


@app.route("/login")
def login():
    title = "Login"
    return render_template("login.html", title=title)


@app.route("/addme", methods=["GET", "POST"])
def addme():
    title = "Add Me"
    if request.method == "POST":
        film = Watched(
            movie=request.form["movie"],
            poster=request.form["poster"],
            watched_date=datetime.strptime(request.form["watched_date"], "%Y-%m-%d"),
            picked_by=request.form["picked_by"],
        )
        db.session.add(film)
        db.session.commit()
        return redirect("/addme")
    else:
        film_lists = Watched.query.order_by(Watched.watched_date.asc()).all()
        return render_template("addme.html", title=title, film_lists=film_lists)


@app.route("/delete/<int:id>")
def delete(id):
    watched_id = Watched.query.get_or_404(id)
    db.session.delete(watched_id)
    db.session.commit()
    return redirect("/addme")


if __name__ == "__main__":
    app.run()
