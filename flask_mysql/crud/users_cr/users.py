from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        users= []
        for one_row in results:
            users.append(cls(one_row))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        #comes back as a new row id
        result = connectToMySQL("users_schema").query_db(query, data)
        return result
        
        