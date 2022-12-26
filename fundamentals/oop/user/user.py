#Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

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
        
    def enroll(self):
        
        if self.is_rewards_member:
            print("User already a member")
            return False

        
        self.gold_card_points = 200
        self.is_rewards_member = True
        #Changed 0 to 200 
        #Changed from False to True
    
        

    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You do not have enough")
            return
        
        #self.gold_card_points -= amount
        self.gold_card_points = self.gold_card_points - amount

        
user_joshua = User("Joshua", "Rosado","joshua06rosado@gmail.com", 28)
user_alexis = User("Alexis","Rosado", "alexis.ruff.970@gmail.com", 26)


user_joshua.display_info()
user_joshua.enroll()
user_joshua.display_info()
user_joshua.spend_points(75)
user_joshua.display_info()
user_joshua.spend_points(126)
user_joshua.display_info()

user_alexis.enroll()
user_alexis.spend_points(100)
user_alexis.display_info()



#===========================================================================#

# # Assignment: User
# # For this assignment you will create the user class and add a couple methods!

# ####### Note: NOT ALL CODE FROM THE VIDEO IS PROVIDED #######

# class User:

#     def __init__(self, first_name, last_name, email, age):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.is_rewards_member = False
#         self.gold_card_points = 0

#     # Methods:
#     # display_info(self) - Have this method print all 
#     # of the users' details on separate lines.

#     def display_info(self):
#         print("==========================")
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Email: {self.email}")
#         print(f"Age: {self.age}")
#         print(f"Member: {self.is_rewards_member}")
#         print(f"Current Points: {self.gold_card_points}")
#         print("==========================")

#     def enroll(self):

#         # NINJA BONUS
#         # Add logic in the enroll method to check if 
#         # they are a member already, and if they are, 
#         # print "User already a member." and return False, otherwise return True.

#         # REGULAR STUFF

#         # Have this method change the user's member
#         # status to True and 
#         self.is_rewards_member = True

#         # set their gold card points to 200.
#         #######   You can do it!


    
    
#     def spend_points(self, amount):

#         # Add logic in the spend points method
#         # to be sure they have enough points to 
#         # spend that amount and handle appropriately.
        
#         # PSEUDO CODE FOR NINJA BONUS
#         # if they don't have enough points:
#             # print to the console -- "You don't have enough points."
#             # then return # exit function!

#         # decrease the user's points by the amount specified.
#         self.gold_card_points
#         # .... this line is incomplete .. how do set this to a new value?

    

#     # Ninja Bonuses:



# my_user = User("Sadie", "Flick", "sflick@codingdojo.com", 99)
# my_user.display_info()
# my_user.enroll()
# my_user.display_info()
# my_user.spend_points(100)
# my_user.display_info()




