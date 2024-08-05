from item import Item

class Room():

    number_of_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self._description = None
        self.linked_rooms = {}
        self.character = []
        Room.number_of_rooms = Room.number_of_rooms + 1
        self._item = []

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, room_description):
        if len(room_description) < 500:
            self._description = room_description

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item_name):
        if isinstance(item_name, Item):
            self._item.append(item_name)
        else:
            self._item = item_name

    def describe(self):
        print(self.description)

    def set_character(self, new_character):
        self.character.append(new_character)        

    def get_character(self):
        return self.character

    def remove_character(self, old_character):
        self.character.remove(old_character)

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def link_room(self, room_to_link, direction, unlocked):
        self.linked_rooms[direction] = [room_to_link, unlocked]

    def get_details(self):
        print("The " + self.name)
        print("-------------------")
        print(self.description)
        print("")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room[0].get_name() + " is " + direction + ".")
            if not room[1]:
                print("This passage is locked.")

    def move(self, direction):
        if direction in self.linked_rooms:
            data = self.linked_rooms[direction]
            if data[1]:
                return [data[0], True]
            else:
                print("This passage is locked. You cannot pass.")
                return [self, False]
        else:
            print("You can't go that way")
            return [self, False]

    def lock(self, direction):
        if direction in self.linked_rooms:
            self.linked_rooms[direction][1] = not self.linked_rooms[direction][1]
            other = self.linked_rooms[direction][0]
            directions = ["east", "north", "south", "west"]
            index = directions.index(direction)
            index = 3 - index
            thing = directions[index]
            other.linked_rooms[thing][1] = not other.linked_rooms[thing][1]
            if self.linked_rooms[direction][1]:
                print("The door has now been unlocked!")
            else:
                print("The door has now been locked!")
        else:
            print("There is no door in that direction.")
