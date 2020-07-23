# 1. The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [num for num in L if num > 10]

# 2. Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites = list(filter((lambda x: len(x[0]) > 3 and len(x[1]) > 3), zip(l1, l2)))

# 3. requests-11-1: If you wanted to search for photos tagged with either river or mountains, rather than requiring both, what would you change in the code?

# C. Set ``params_diction["tag_mode"] = "any"

# 4. requests-12-1: When you have non-ASCII characters in a string and you get an error trying to write them, which method should you invoke on the string?

# A. ``.encode()``

# 5. The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.
#    Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.
#    For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!".
#    Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
        
    def action(self):
        return '{} knows a lot of different moves!'.format(self.name)
    
p1 = Grass_Pokemon('Belle')
    
