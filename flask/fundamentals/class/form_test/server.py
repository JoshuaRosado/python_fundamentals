from flask import Flask, render_template, request, redirect, session #ADDED request, redirect, session
app = Flask (__name__)
app.secret_key="Waves are breaking left!"  # set a secret key for security purposes






# our index route will handle rendering our form
#Because the create_user method is the method in which we receive the information from the POST request, let's write the information to session in this method:
@app.route('/users', methods=['POST'])
def create_user():
    print("Got POST Info")
    session['username'] = request.form["name"]
    session['useremail'] = request.form["email"]
    # print(request.form)
    # name = request.form["name"]
    # email = request.form["email"]
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/show')


#Previously in our show_user function, we didn't have access to the name and email from the form submission. Now, because of session, we have a way to access the name and email in a different function!

# Let's modify our show_user function:


# @app.route('/show')
# def show_user():
#     # print("Showing the user info from the FORM")
#     # print(request.form)
#     return render_template("show.html",name_on_template = session['username'],email_on_template = session['useremail'])


@app.route('/show')
def show_user():
    return render_template('show.html')




# @app.route('/')
# def index():
#     return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port= 5001)
    