from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.car import Car
from flask import flash


@app.route("/cars/home")
def cars_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    
    user = User.get_by_id(session["user_id"])
    cars = Car.get_all()

    return render_template("home.html", user=user, cars=cars)

@app.route("/cars/<int:car_id>")
def car_detail(car_id):
    user = User.get_by_id(session["user_id"])
    car = Car.get_by_id(car_id)
    return render_template("car_detail.html", user=user, car=car)

@app.route("/cars/new")
def car_create_page():
    return render_template("add_car.html")


@app.route("/cars/edit/<int:car_id>")
def car_edit_page(car_id):
    car = Car.get_by_id(car_id)
    return render_template("edit_car.html", car=car)

    
@app.route("/cars", methods=["POST"])
def add_car():
    valid_car = Car.add_valid_car(request.form)
    if valid_car:
        return redirect(f'/cars/home')
    return redirect('/cars/new')

@app.route("/cars/<int:car_id>", methods=["POST"])
def update_car(car_id):

    valid_car = Car.update_car(request.form, session["user_id"])

    if not valid_car:
        return redirect(f"/cars/edit/{car_id}")
        
    return redirect(f"/cars/home")

@app.route("/cars/delete/<int:car_id>")
def delete_by_id(car_id):
    Car.delete_car_by_id(car_id)
    return redirect("/cars/home")

