from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree
from flask import flash


@app.route("/trees/home")
def trees_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    
    user = User.get_by_id(session["user_id"])
    trees = Tree.get_all()

    return render_template("home.html", user=user, trees=trees)

@app.route("/trees/<int:tree_id>")
def tree_detail(tree_id):
    user = User.get_by_id(session["user_id"])
    tree = Tree.get_by_id(tree_id)
    return render_template("tree_detail.html", user=user, tree=tree)

@app.route("/trees/create")
def tree_create_page():
    return render_template("create_tree.html")


@app.route("/trees/edit/<int:tree_id>")
def tree_edit_page(tree_id):
    tree = tree.get_by_id(tree_id)
    return render_template("edit_tree.html", tree=tree)


@app.route("/trees", methods=["POST"])
def create_tree():
    valid_tree = Tree.create_valid_tree(request.form)
    if valid_tree:
        return redirect(f'/trees/{valid_tree.id}')
    return redirect('/trees/create')

@app.route("/trees/<int:tree_id>", methods=["POST"])
def update_tree(tree_id):

    valid_tree = Tree.update_tree(request.form, session["user_id"])

    if not valid_tree:
        return redirect(f"/trees/edit/{tree_id}")
        
    return redirect(f"/trees/{tree_id}")

@app.route("/trees/delete/<int:tree_id>")
def delete_by_id(tree_id):
    Tree.delete_tree_by_id(tree_id)
    return redirect("/trees/home")