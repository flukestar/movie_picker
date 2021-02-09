from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import imdbscrapper

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mysite.db"
db = SQLAlchemy(app)


class Watched(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(200), nullable=False)
    watched_date = db.Column(db.String(20), nullable=False)
    picked_by = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Watched(movie='%s', watched_date='%s', picked_by='%s')>" % (
            self.movie,
            self.watched_date,
            self.picked_by,
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


@app.route("/seen", methods=["GET", "POST"])
def seen():
    title = "Seen"
    if request.method == "POST":
        film = Watched(
            movie=request.form["movie"],
            watched_date=request.form["watched_date"],
            picked_by=request.form["picked_by"],
        )
        db.session.add(film)
        db.session.commit()
        return redirect("/seen")
    else:
        film_lists = Watched.query.all()
        return render_template("watched.html", title=title, film_lists=film_lists)


@app.route("/delete/<int:id>")
def delete(id):
    watched_id = Watched.query.get_or_404(id)
    db.session.delete(watched_id)
    db.session.commit()
    return redirect("/seen")

if __name__ == "__main__":
    app.run()