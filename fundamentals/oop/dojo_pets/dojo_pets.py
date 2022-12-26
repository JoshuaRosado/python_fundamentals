
class Ninja:
    def __init__(self, first_name, last_name, pet, threats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.threats = threats
        self.pet_food = pet_food
        
#  # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

## feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) > 0: #if the lenght of pet_food is more than 0
            food = self.pet_food.pop() #food equals for pet_food to disappear because the pet ate it
            print(f"Feeding {self.pet.name} {food}!") # Print Feeding (pet's name) (food)
            self.pet.eat() # invoke pet eat () method
        else:
            [print(f"OH OH!!!! we need to get more food {self.pet.name}")]
            return self
    
# # bathe() - cleans the ninja's pet invoking the pet noise() method
    

    def bathe(self):
        self.pet.noise()
        print(f"That's {self.pet.name}making{self.pet.noise}")
        return self

# # implement __init__( name , type , tricks ):
class Pet:
    def __init__(self, name, type, tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 90
        self.noise = noise
    
    def __repr__(self):
        return self
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
        
# # play() - increases the pet's health by 5
        
    def play(self):
        self.health += 5
        self.energy -= 20
        return self
        
# # noise() - prints out the pet's sound
    def noise(self):
        self.pet.noise()
        return self

    
Luther = Pet("Luther", "Dog",["Jumps", "Runs", "Swims"],"Woof Woof!")
my_threats = ["Scooby Snacks", "Bacon Bites", "Carrots"]
pet_food = ["Dog Food", "Veggies", "Fruits"]
joshua = Ninja("Joshua", "Rosado", Luther ,my_threats, pet_food)


joshua.feed(); 
joshua.feed();
joshua.feed();
joshua.feed()


