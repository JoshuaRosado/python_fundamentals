from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

DB = "car_dealz"

class Car:
    
    def __init__(self, car):
        self.id = car["id"]
        self.price = car["price"]
        self.model = car["model"]
        self.make = car["make"]
        self.year = car["year"]
        self.description = car["description"]
        self.created_at = car["created_at"]
        self.updated_at = car["updated_at"]
        self.user = None

    @classmethod
    def add_valid_car(cls, car_dict):
        if not cls.is_valid(car_dict):
            return False
        
        query = """INSERT INTO cars(price, model, make, year, description, user_id) VALUES  (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s);"""
        car_id = connectToMySQL(DB).query_db(query, car_dict)
        car = cls.get_by_id(car_id)

        return car 

    @classmethod
    def get_by_id(cls, car_id):
        print(f"get car by id {car_id}")
        data = {"id": car_id}
        query = """SELECT cars.id, cars.created_at, cars.updated_at, make, model, price, year, description,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM cars
                    JOIN users on users.id = cars.user_id
                    WHERE cars.id = %(id)s;"""
        
        result = connectToMySQL(DB).query_db(query, data)
        print("result of query:")
        print(result)
        result = result[0]
        car = cls(result)
        
        

        car.user = user.User(
                {
                    "id": result["user_id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "email": result["email"],
                    "password": False,
                    "created_at": result["uc"],
                    "updated_at": result["uu"]
                }
            )

        return car

    @classmethod
    def delete_car_by_id(cls, car_id):

        data = {"id": car_id}
        query = "DELETE from cars WHERE id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)

        return car_id


    @classmethod
    def update_car(cls, car_dict, session_id):


        car = cls.get_by_id(car_dict["id"])
        if car.user.id != session_id:
            flash("You must be the creator to update this car.")
            return False


        if not cls.is_valid(car_dict):
            return False
        

        query = """UPDATE cars
                    SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description= %(description)s 
                    WHERE id = %(id)s;"""
        result = connectToMySQL(DB).query_db(query,car_dict)
        car = cls.get_by_id(car_dict["id"])
        
        return car

    @classmethod
    def get_all(cls):
        query = """SELECT 
                    cars.id, cars.created_at, cars.updated_at, price, model, make, year, description,
                    users.id as user_id, first_name, last_name, email,password, users.created_at as uc, users.updated_at as uu
                    FROM cars
                    JOIN users on users.id = cars.user_id;"""
        car_data = connectToMySQL(DB).query_db(query)


        cars = []

        for car in car_data:

            
            car_obj = cls(car)

            car_obj.user = user.User(
                {
                    "id": car["user_id"],
                    "first_name": car["first_name"],
                    "last_name": car["last_name"],
                    "email": car["email"],
                    "password": True,
                    "created_at": car["uc"],
                    "updated_at": car["uu"]
                }
            )
            cars.append(car_obj)


        return cars

    @staticmethod
    def is_valid(car_dict):
        valid = True
        if len(car_dict["price"]) <=0:
            flash(" Price must be greater than 0.")
            valid = False
        if len(car_dict["model"]) <=0:
            flash("Model Field required!.")
            valid = False
        if len(car_dict["make"]) <= 0:
            flash(" Make Field required!")
            valid = False
        if len(car_dict["year"]) <= 0:
            flash("Year field must be greater than 0.")
            valid = False
        if len(car_dict["description"]) <= 0:
            flash("Description Field required.")
            valid = False

        return valid
        