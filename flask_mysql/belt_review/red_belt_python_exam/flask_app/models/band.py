from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

DB = "band_together"

class Band:
    
    def __init__(self, band):
        self.id = band["id"]
        self.band_name = band["band_name"]
        self.music_genre = band["music_genre"]
        self.home_city = band["home_city"]
        self.created_at = band["created_at"]
        self.updated_at = band["updated_at"]
        self.user = None

    @classmethod
    def create_valid_band(cls, band_dict):
        if not cls.is_valid(band_dict):
            return False
        
        
        query = """INSERT INTO bands(band_name, music_genre, home_city, user_id) VALUES  (%(band_name)s, %(music_genre)s, %(home_city)s, %(user_id)s);"""
        band_id = connectToMySQL(DB).query_db(query, band_dict)
        band = cls.get_by_id(band_id)

        return band
    
    
    @classmethod
    def get_by_id(cls, band_id):
        print(f"get band by id {band_id}")
        data = {"id": band_id}
        query = """SELECT bands.id, bands.created_at, bands.updated_at,band_name, music_genre, home_city,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM bands
                    JOIN users on users.id = bands.user_id
                    WHERE bands.id = %(id)s;"""
        
        result = connectToMySQL(DB).query_db(query, data)
        print("result of query:")
        print(result)
        result = result[0]
        band = cls(result)
        
        

        band.user = user.User(
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

        return band

    @classmethod
    def delete_band_by_id(cls, band_id):

        data = {"id": band_id}
        query = "DELETE from bands WHERE id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)

        return band_id


    @classmethod
    def update_band(cls, band_dict, session_id):


        band = cls.get_by_id(band_dict["id"])
        if band.user.id != session_id:
            flash("You must be the creator to update this band.")
            return False


        if not cls.is_valid(band_dict):
            return False
        

        query = """UPDATE bands
                    SET band_name = %(band_name)s, music_genre = %(music_genre)s, home_city = %(home_city)s
                    WHERE id = %(id)s;"""
        result = connectToMySQL(DB).query_db(query,band_dict)
        band = cls.get_by_id(band_dict["id"])
        
        return band

    @classmethod
    def get_all(cls):
        query = """SELECT 
                    bands.id, bands.created_at, bands.updated_at, band_name, music_genre, home_city,
                    users.id as user_id, first_name, last_name, email,password, users.created_at as uc, users.updated_at as uu
                    FROM bands
                    JOIN users on users.id = bands.user_id;"""
        band_data = connectToMySQL(DB).query_db(query)


        bands = []

        for band in band_data:

            
            band_obj = cls(band)

            band_obj.user = user.User(
                {
                    "id": band["user_id"],
                    "first_name": band["first_name"],
                    "last_name": band["last_name"],
                    "email": band["email"],
                    "password": True,
                    "created_at": band["uc"],
                    "updated_at": band["uu"]
                }
            )
            bands.append(band_obj)


        return bands

    @staticmethod
    def is_valid(band_dict):
        valid = True
        if len(band_dict["band_name"]) < 2:
            flash(" Band Name field must be greater than 2.")
            valid = False
        if len(band_dict["music_genre"]) < 2:
            flash("Music Genre field must be greater than 2.")
            valid = False
        if len(band_dict["home_city"]) <= 0:
            flash(" Home City field is required!")
            valid = False

        return valid
        