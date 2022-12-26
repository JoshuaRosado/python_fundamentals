from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html", col=8, row=8,color_one= "red", color_two="black")

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", col=8, row=x, color_one="red", color_two="black")

@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template("index.html", col=y, row=x, color_one="red", color_two="black")

@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x, y, one):
    return render_template("index.html", col=y, row=x, color_one=one, color_two="black")

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x, y, one, two):
    return render_template("index.html", col=y, row=x, color_one=one, color_two=two)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port =5001)