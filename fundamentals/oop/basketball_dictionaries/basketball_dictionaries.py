from unicodedata import name


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "Jah Morant", 
        "age":25, 
        "position": "Point Guard", 
        "team": "Memphis Grizzlies"
    }
]


# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

#UPDATED
class Player:  # = dict
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict ["position"]
        self.team = dict ["team"]
    
    def __repr__(self):
        return (f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")
    
    # NINJA BONUS class method
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects
        
        
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
print(player_kevin)
player_jason = Player(jason)
print(player_jason)
player_kyrie = Player(kyrie)
print(player_kyrie)



#Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.


# for loop over the list of dictionaries
#each time use that dictionary info
# to create a new player instance
new_team_list = []
for dict in players:
    player = Player(dict)
    new_team_list.append(player)
    
print(new_team_list)
    
    