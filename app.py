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
<<<<<<< HEAD
<<<<<<< HEAD
=======
@app.route("/watchlist", methods=["GET", "POST"])
=======
@app.route("/watched", methods=["GET", "POST"])
>>>>>>> sqllite_db_feature
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
        return redirect("/watched")
    else:
        film_lists = Watched.query.all()
        return render_template("watched.html", title=title, film_lists=film_lists)


@app.route("/delete/<int:id>")
def delete(id):
    watched_id = Watched.query.get_or_404(id)
    db.session.delete(watched_id)
    db.session.commit()
<<<<<<< HEAD
    return redirect("/watchlist")


>>>>>>> d17d991 (removed old comments from app.py)
=======
>>>>>>> 7891faad2427434f2032f4f7ad61a26d4e05b395
=======
    return redirect("/watched")


>>>>>>> sqllite_db_feature
if __name__ == "__main__":
    app.run()