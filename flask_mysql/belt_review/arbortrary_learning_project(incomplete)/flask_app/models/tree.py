from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

DB = "tree_schema"

class Tree:
    
    def __init__(self, tree):
        self.id = tree["id"]
        self.name = tree["tree_species"]
        self.description = tree["location"]
        self.instructions = tree["reason"]
        self.date_made = tree["date_planted"]
        self.created_at = tree["created_at"]
        self.updated_at = tree["updated_at"]
        self.user = None

    @classmethod
    def create_valid_tree(cls, tree_dict):
        if not cls.is_valid(tree_dict):
            return False
        
        query = """INSERT INTO trees (tree_species, location, reason, date_planted, user_id) VALUES (%(tree_species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);"""
        tree_id = connectToMySQL(DB).query_db(query, tree_dict)
        tree = cls.get_by_id(tree_id)

        return tree

    @classmethod
    def get_by_id(cls, tree_id):
        print(f"get tree by id {tree_id}")
        data = {"id": tree_id}
        query = """SELECT trees.id, trees.created_at, trees.updated_at, tree_species, location, reason, date_planted,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM trees
                    JOIN users on users.id = trees.user_id
                    WHERE trees.id = %(id)s;"""
        
        result = connectToMySQL(DB).query_db(query,data)
        print("result of query:")
        print(result)
        result = result[0]
        tree = cls(result)
        

        tree.user = user.User(
                {
                    "id": result["user_id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "email": result["email"],
                    "created_at": result["uc"],
                    "updated_at": result["uu"]
                }
            )

        return tree

    @classmethod
    def delete_tree_by_id(cls, tree_id):

        data = {"id": tree_id}
        query = "DELETE from trees WHERE id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)

        return tree_id


    @classmethod
    def update_tree(cls, tree_dict, session_id):


        tree = cls.get_by_id(tree_dict["id"])
        if tree.user.id != session_id:
            flash("You must be the creator to update this tree.")
            return False


        if not cls.is_valid(tree_dict):
            return False
        

        query = """UPDATE trees
                    SET tree_species = %(tree_species)s, location = %(location)s, reason = %(reason)s, date_planted=%(date_planted)s 
                    WHERE id = %(id)s;"""
        result = connectToMySQL(DB).query_db(query,tree_dict)
        tree = cls.get_by_id(tree_dict["id"])
        
        return tree

    @classmethod
    def get_all(cls):
        query = """SELECT 
                    trees.id, trees.created_at, trees.updated_at, tree_species, location, reason, date_planted,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM trees
                    JOIN users on users.id = trees.user_id;"""
        tree_data = connectToMySQL(DB).query_db(query)


        trees = []

        for tree in tree_data:

            
            tree_obj = cls(tree)

            tree_obj.user = user.User(
                {
                    "id": tree["user_id"],
                    "first_name": tree["first_name"],
                    "last_name": tree["last_name"],
                    "email": tree["email"],
                    "created_at": tree["uc"],
                    "updated_at": tree["uu"]
                }
            )
            trees.append(tree_obj)


        return trees

    @staticmethod
    def is_valid(tree_dict):
        valid = True
        flash_string = " field is required and must be at least 3 characters."
        if len(tree_dict["tree_species"]) < 5:
            flash("Tree Species " + flash_string)
            valid = False
        if len(tree_dict["location"]) < 2:
            flash("Location" + flash_string)
            valid = False
        if len(tree_dict["reason"]) > 50:
            flash("Reason " + flash_string)
            valid = False

        if len(tree_dict["date_planted"]) <= 0:
            flash("Date is required.")
            valid = False

        return valid
        