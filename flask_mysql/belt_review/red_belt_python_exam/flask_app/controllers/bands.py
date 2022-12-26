from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.band import Band
from flask import flash


@app.route("/bands/home")
def bands_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    
    user = User.get_by_id(session["user_id"])
    bands = Band.get_all()

    return render_template("home.html", user=user, bands=bands)

@app.route("/bands/my_bands")
def my_bands():
    if "user_id" not in session:
        flash("You must be logged in to access the my bands")
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    band = Band.get_all()
    
    return render_template("band_detail.html", user=user, band=band)

@app.route("/bands/my_bands/<int:band_id>")
def bands_page(band_id):
    band = Band.get_by_id(band_id)
    user = User.get_by_id(session["user_id"])
    return render_template("band_detail.html", band=band, user=user)














@app.route("/bands/new")
def band_create_page():
    user= User.get_by_id(session['user_id'])
    band= Band.get_all()
    return render_template("add_band.html", user=user, band=band)


@app.route("/bands", methods=["POST"])
def add_band():
    valid_band = Band.create_valid_band(request.form)
    if valid_band:
        return redirect(f'/bands/home')
    return redirect('/bands/new')











@app.route("/bands/edit/<int:band_id>")
def band_edit_page(band_id):
    band = Band.get_by_id(band_id)
    return render_template("edit_band.html", band=band)





@app.route("/bands/<int:band_id>", methods=["POST"])
def update_band(band_id):

    valid_band = Band.update_band(request.form, session["user_id"])

    if not valid_band:
        return redirect(f"/bands/edit/{band_id}")
        
    return redirect(f"/bands/home")

@app.route("/bands/delete/<int:band_id>")
def delete_by_id(band_id):
    Band.delete_band_by_id(band_id)
    return redirect("/bands/home")

