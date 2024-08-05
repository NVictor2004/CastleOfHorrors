from random import randint, shuffle
from room import Room

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.room_current = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        print("[" + self.name + " says]: " + self.conversation)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)

    def set_room(self, room_thing):
        self.room_current = room_thing

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you.")
        return True

    def move(self):
        data = []
        thing = self.room_current.linked_rooms
        for direction in thing:
            data.append(direction)

        shuffle(data)
        for direction in data:
            if thing[direction][1]:
                a = self.room_current
                self.room_current = thing[direction][0]
                return [a, self.room_current, True]
        return [self.room_current, self.room_current, False]

class Enemy(Character):
    num_enemies = 0
    
    def __init__(self, char_name, char_description, fighting_item, max_strength):
        super().__init__(char_name, char_description)
        self.max_strength = max_strength
        self.strength = randint(0, max_strength)
        Enemy.num_enemies = Enemy.num_enemies + 1
        self.weapon = fighting_item
        self.lives = 3

    def describe(self):
        super().describe()
        print("This is an Enemy!")

    def fight(self, combat_item, xp):
        zombie_strength = self.strength + self.weapon.strength
        player_strength = xp + combat_item.strength
        combat_item.strength = combat_item.strength - 5
        self.weapon.strength = self.weapon.strength - 5
        if player_strength >= zombie_strength:
            print("You fend " + self.name + " off with the " + combat_item.name)
            self.lives = self.lives - 1
            self.strength = randint(0, self.max_strength)
            return [False, self.lives]
        else:
            print(self.name + " is too strong for you. You lose a life.")
            return [True, self.lives]
            

class Master(Enemy):
    num_masters = 0
    
    def __init__(self, char_name, char_description, fighting_item, max_strength):
        super().__init__(char_name, char_description, fighting_item, max_strength)
        Master.num_masters = Master.num_masters + 1
        Enemy.num_enemies = Enemy.num_enemies - 1
        self.lives = 5

    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        print("[" + self.name + " says]: " + self.conversation)
        print("This is the Master!")

class Friend(Character):
    def __init__(self, char_name, char_description, return_trade):
        super().__init__(char_name, char_description)
        self.return_trading_items = [return_trade]

    def hug(self):
        print("You hug", self.name)
        print("You feel happy now.")

    def describe(self):
        super().describe()
        print("This is a Friend!")

    def trade(self, trading_items):
        print(self.name, "gives you all of his belongings in exchange.")
        print("")
        a = self.return_trading_items
        self.return_trading_items = []
        for thing in trading_items:
            self.return_trading_items.append(thing)
        return a


