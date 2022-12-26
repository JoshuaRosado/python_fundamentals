#Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

from ast import Return


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
# display_info(self) - Have this method print all 
# of the users' details on separate lines.        
    def display_info(self):
        print("**********************************")
        print(f"First Name:{self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Active Member: {self.is_rewards_member}")
        print(f"Points Available: {self.gold_card_points}")
        print("**********************************")
        
        return self
    
    
    def enroll(self):
        
        if self.is_rewards_member:
            print("User already a member")
            return False

        
        self.gold_card_points = 200
        self.is_rewards_member = True
        #Changed 0 to 200 
        #Changed from False to True
        
        return self

    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You do not have enough")
            return 
        
        #self.gold_card_points -= amount
        self.gold_card_points = self.gold_card_points - amount
        
        return self
        
user_joshua = User("Joshua", "Rosado","joshua06rosado@gmail.com", 28)
user_alexis = User("Alexis","Rosado", "alexis.ruff.970@gmail.com", 26)


# user_joshua.display_info()
# user_joshua.enroll()
# user_joshua.display_info()
# user_joshua.spend_points(75)
# user_joshua.display_info()
# user_joshua.spend_points(126)
# user_joshua.display_info()

# user_alexis.enroll()
# user_alexis.spend_points(100)
# user_alexis.display_info()

user_joshua.display_info().enroll().display_info().spend_points(75).display_info().spend_points(126).display_info()




user_alexis.enroll().spend_point(100).display_info() 


