from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

from users import User

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
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 5001)