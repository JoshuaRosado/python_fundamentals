from crypt import methods
from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key="Waves are breaking left"

@app.route('/')
def index():
    if "num" not in session:
        session["num"] = random.randint(1, 100)
        
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5001)