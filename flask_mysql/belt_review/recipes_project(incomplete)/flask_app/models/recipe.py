# import the function that will return an instance of a connection
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

DB = "recipes"

class Recipe:
    
    def __init__(self, recipe):
        self.id = recipe["id"]
        self.name = recipe["name"]
        self.description = recipe["description"]
        self.instructions = recipe["instructions"]
        self.date_made = recipe["date_made"]
        self.under_30 = recipe["under_30"]
        self.created_at = recipe["created_at"]
        self.updated_at = recipe["updated_at"]
        self.user = None

    @classmethod
    def create_valid_recipe(cls, recipe_dict):
        if not cls.is_valid(recipe_dict):
            return False
        
        query = """INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"""
        recipe_id = connectToMySQL(DB).query_db(query, recipe_dict)
        recipe = cls.get_by_id(recipe_id)

        return recipe

    @classmethod
    def get_by_id(cls, recipe_id):
        print(f"get recipe by id {recipe_id}")
        data = {"id": recipe_id}
        query = """SELECT recipes.id, recipes.created_at, recipes.updated_at, instructions, description, name, date_made, under_30,
                    users.id as user_id, first_name, last_name, email,password, users.created_at as uc, users.updated_at as uu
                    FROM recipes
                    JOIN users on users.id = recipes.user_id
                    WHERE recipes.id = %(id)s;"""
        
        result = connectToMySQL(DB).query_db(query,data)
        print("result of query:")
        print(result)
        result = result[0]
        recipe = cls(result)
        
        # convert joined user data into a user object
        recipe.user = user.User(
                {
                    "id": result["user_id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "email": result["email"],
                    "password": result["password"],
                    "created_at": result["uc"],
                    "updated_at": result["uu"]
                }
            )

        return recipe

    @classmethod
    def delete_recipe_by_id(cls, recipe_id):

        data = {"id": recipe_id}
        query = "DELETE from recipes WHERE id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)

        return recipe_id


    @classmethod
    def update_recipe(cls, recipe_dict, session_id):

        # Authenticate User first
        recipe = cls.get_by_id(recipe_dict["id"])
        if recipe.user.id != session_id:
            flash("You must be the creator to update this recipe.")
            return False

        # Validate the input
        if not cls.is_valid(recipe_dict):
            return False
        
        # Update the data in the database.
        query = """UPDATE recipes
                    SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made=%(date_made)s, under_30 = %(under_30)s
                    WHERE id = %(id)s;"""
        result = connectToMySQL(DB).query_db(query,recipe_dict)
        recipe = cls.get_by_id(recipe_dict["id"])
        
        return recipe

    @classmethod
    def get_all(cls):
        # Get all recipes, and the user info for the creators
        query = """SELECT 
                    recipes.id, recipes.created_at, recipes.updated_at, instructions, description, name, date_made, under_30,
                    users.id as user_id, first_name, last_name, email, password, users.created_at as uc, users.updated_at as uu
                    FROM recipes
                    JOIN users on users.id = recipes.user_id;"""
        recipe_data = connectToMySQL(DB).query_db(query)

        # Make a list to hold recipe objects to return
        recipes = []

        # Iterate through the list of recipe dictionaries
        for recipe in recipe_data:

            # convert data into a recipe object
            recipe_obj = cls(recipe)

            # convert joined user data into a user object
            recipe_obj.user = user.User(
                {
                    "id": recipe["user_id"],
                    "first_name": recipe["first_name"],
                    "last_name": recipe["last_name"],
                    "email": recipe["email"],
                    "password": recipe["password"],
                    "created_at": recipe["uc"],
                    "updated_at": recipe["uu"]
                }
            )
            recipes.append(recipe_obj)


        return recipes

    @staticmethod
    def is_valid(recipe_dict):
        valid = True
        flash_string = " field is required and must be at least 3 characters."
        if len(recipe_dict["name"]) < 3:
            flash("Name " + flash_string)
            valid = False
        if len(recipe_dict["description"]) < 3:
            flash("Description " + flash_string)
            valid = False
        if len(recipe_dict["instructions"]) < 3:
            flash("Instructions " + flash_string)
            valid = False

        if len(recipe_dict["date_made"]) <= 0:
            flash("Date is required.")
            valid = False
        if "under_30" not in recipe_dict:
            flash("Does your recipe take less than 30 min?")
            valid = False

        return valid
        