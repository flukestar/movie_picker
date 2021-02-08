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


<<<<<<< HEAD
=======
@app.route("/watchlist", methods=["GET", "POST"])
def watchlist():
    title = "Watched List"
    if request.method == "POST":
        film = Watched(
            movie=request.form["movie"],
            watched_date=request.form["watched_date"],
            picked_by=request.form["picked_by"],
        )
        db.session.add(film)
        db.session.commit()
        return redirect("/watchlist")
    else:
        film_lists = Watched.query.all()
        return render_template("watchlist.html", title=title, film_lists=film_lists)


@app.route("/delete/<int:id>")
def delete(id):
    watched_id = Watched.query.get_or_404(id)
    db.session.delete(watched_id)
    db.session.commit()
    return redirect("/watchlist")


>>>>>>> d17d991 (removed old comments from app.py)
if __name__ == "__main__":
    app.run()