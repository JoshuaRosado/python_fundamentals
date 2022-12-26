from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key="Waves are breaking left!"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session["count"] += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port= 5001)