from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "Waves are breaking izquierda"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["name"] = request.form["name"] # FOR NAME
    session["location"] = request.form["location"] # FOR LOCATION
    session["language"] = request.form["language"] # FOR LANGUAGE
    session["comment"] = request.form["comment"] # COMMENT
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html")





if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port = 5001)