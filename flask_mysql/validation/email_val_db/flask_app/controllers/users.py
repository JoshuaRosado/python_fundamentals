from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")






@app.route('/user/create', methods=["POST"])
def create():

#Check if the form info is valid input
    if User.is_valid_user(request.form):
        #>>>>>>WHATEVER THE USER TYPED IN (request.form = DICTIONARY)<<<<<<
    #if User is valid, we're gonna create a User in the DATABASE
        User.save(request.form)
        return redirect ('/')
#create the user if valid
#If not send direct user back to the create page
    else:

    
#to be able to show them messages(FLASH) if they have something wrong
        return redirect('/user/new')







@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html" , user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')




