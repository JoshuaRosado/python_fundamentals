from urllib import request
from flask_app import app
from flask import render_template, request, redirect, session

@app.route('/cities/new')
def new_city_form():
    return render_template("new_city.html")

@app.route('/cities/add_to_db', methods= ['POST'])
def add_city_to_db():
    print(request.form) #Print the mayor of the city from the FORM
    
    session["mayor"] = request.form["mayor"]
    session["name"] = request.form["name"]
    session["population"] = request.form["population"]
    return render_template('/cities/show_city')

@app.route('/cities/show_city')
def show_city():
    print(request.form)
    
    return render_template("show_city.html", mayor= request.form['mayor'], city=request.form['name'], population=request.form['population'])