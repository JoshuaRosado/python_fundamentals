from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
        
        # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html")  # Return the string 'Hello World!' as a response   # Ensure this file is being run directly and not from a different module    
# Run the app in debug mode.

@app.route('/About')
def about():
    return ("Want to know more about us?")


# RENDERING DATA ON TEMPLATE
@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return render_template("hello.html", name= name, num= num)





# @app.route('/hi/<username>/<int:num>')
# def hi(username, num):
#     return f"Hi {username * num}"


# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id


@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id






@app.route('/lists')
def render_lists():
    student_info = [
        {"name": "Michael", "age": 35},
        {"name": "John", "age": 30},
        {"name": "Mark", "age": 25},
        {"name": "KB", "age": 27}
    ]
    return render_template("lists.html", random_numbers= [3,1,5], students= student_info)
    


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0', port= 5001)
