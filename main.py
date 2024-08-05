from room import Room
from item import Item
from character import Enemy, Friend, Character, Master
from rpginfo import RPGInfo
from re import search
from random import randint

# 115
def instructions():
    print("")
    print("If you want to move to a different room, type the direction that you want to move in (north, east, south, west).")
    print("If you want to pick up an item, type (item).")
    print("If you want to view what is in your backpack, type (reveal).")
    print("If you want to lock a passageway, type (lock). However, you need a Skeleton Key to do this.")
    print("If you want to restore all of your lives, type (medicine). However, you need Medicine to do this.")
    print("If there is a Friend in the room, you can hug them (hug), trade with them (trade) or talk to them (discuss).")
    print("")
    print("Whenever you are in the same room as an Enemy, he will challenge you to a fight!")
    print("Make sure you have strong weapons in your backpack and a large amount of XP, otherwise you will lose a life!")
    print("XP can be gained by picking up items, hugging, trading, talking and winning fights.")
    print("Whenever you use an Item as a weapon, it's strength will decrease. So don't rely on one weapon alone!")
    print("")
    print("If you wish to see the instructions again, type (instruct).")

def moving_zombies(zombies):
    for zombie in zombies:
        room_to_go = zombie.move()
        if room_to_go[2]:
            room_to_go[1].set_character(zombie)
            room_to_go[0].remove_character(zombie)

kitchen=Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies."
ballroom = Room("Ballroom")
ballroom.description = "A place of dangerous frivolity."
dining_hall = Room("Dining room")
dining_hall.description = "A place smelling of rotten fish."
entrance = Room("Entrance Antechamber")
entrance.description = "A small antechamber filled with a sense of neglect and abandonment."
hall = Room("Entrance Hall")
hall.description = "A massive hall lined with dusty tapestries and lit dimly by chandeliers covered in cobwebs."
throne = Room("Throne Room")
throne.description = "The only room in the castle still gleaming with its former glory."
lounge = Room("Lounge")
lounge.description = "An old-fashioned room filled with dusty sofas and broken armchairs."
study = Room("Study")
study.description = "A room so cluttered that the floor is completely covered with cracked files and torn sheets of yellowed paper."
armoury = Room("Armoury")
armoury.description = "A dusty room filled with shining, silver swords and menacing, black warhammers."
barracks = Room("Barracks")
barracks.description = "Sleeping quarters for the Master's undead slaves."
dungeon = Room("Dungeon")
dungeon.description = "The final resting place of all the Master's enemies."
bedroom = Room("Bedroom")
bedroom.description = "The Master's sleeping quarters."
ensuite = Room("Ensuite Bathroom")
ensuite.description = "The Master's personal ensuite bathroom."
bathroom = Room("Bathroom")
bathroom.description = "The public bathroom, filled with massive spiders and murderous smells."
pantry = Room("Pantry")
pantry.description = "A room filled with rotten cakes and delicious wines."

entrance.link_room(hall, "south", True)
hall.link_room(entrance, "north", True)
hall.link_room(throne, "south", True)
throne.link_room(hall, "north", True)
hall.link_room(study, "west", True)
study.link_room(hall, "east", True)
throne.link_room(lounge, "west", True)
lounge.link_room(throne, "east", True)
lounge.link_room(study, "north", True)
study.link_room(lounge, "south", True)
throne.link_room(dining_hall, "east", True)
dining_hall.link_room(throne, "west", True)
dining_hall.link_room(kitchen, "north", True)
kitchen.link_room(dining_hall, "south", True)
hall.link_room(kitchen, "east", True)
kitchen.link_room(hall, "west", True)
throne.link_room(ballroom, "south", True)
ballroom.link_room(throne, "north", True)
dining_hall.link_room(bathroom, "south", True)
bathroom.link_room(dining_hall, "north", True)
barracks.link_room(armoury, "east", True)
armoury.link_room(barracks, "west", True)
armoury.link_room(bedroom, "east", True)
bedroom.link_room(armoury, "west", True)
ensuite.link_room(bedroom, "north", True)
bedroom.link_room(ensuite, "south", True)
ballroom.link_room(armoury, "south", False)
armoury.link_room(ballroom, "north", False)
ballroom.link_room(bathroom, "east", True)
bathroom.link_room(ballroom, "west", True)
barracks.link_room(dungeon, "south", False)
dungeon.link_room(barracks, "north", False)
pantry.link_room(ballroom, "east", True)
ballroom.link_room(pantry, "west", True)
pantry.link_room(lounge, "north", True)
lounge.link_room(pantry, "south", True)

boxing_gloves = Item("Boxing Gloves", 60)
boxing_gloves.description = "They pack a mighty punch!"
entrance.item = boxing_gloves

coat = Item("Winter Jacket", 10)
coat.description = "No better match against the cold!"
hall.item = coat

cloak = Item("Cloak of Invisibility", 10)
cloak.description = "Dave's most powerful possession. Unfortunately, it no longer works, however it is still exceptionally valuable."
bedroom.item = cloak

sword = Item("Sword", 80)
sword.description = "A sharp, pointy weapon."
lounge.item = sword

crossbow = Item("Crossbow", 90)
crossbow.description = "A powerful, dangerous weapon."

book = Item("Book", 30)
book.description = "A book filled with arcane knowledge. Very good for hitting people with."
study.item = book

tapestry = Item("Small Tapestry", 10)
tapestry.description = "A beautiful depiction of Dave's many military successes in life."
throne.item = tapestry

rat = Item("dead rat", 50)
rat.description = "Half eaten."
dungeon.item = rat

club = Item("Club", 40)
club.description = "A pretty powerful weapon."

candlestick = Item("Candlestick", 10)
candlestick.description = "A light in the darkness."
dining_hall.item = candlestick

shampoo = Item("Bottle of Shampoo", 10)
shampoo.description = "Any zombie's top priority: keeping their hair nice and shiny."
bathroom.item = shampoo

pillow = Item("Pillow", 10)
pillow.description = "A formidable weapon indeed."
barracks.item = pillow

slipper = Item("Glass Slipper", 10)
slipper.description = "This once belonged to a princess who came to this castle a long time ago."
ballroom.item = slipper

cheese = Item("Cheese", 10)
cheese.description = "Pretty stinky."
pantry.item = cheese

rubber_ducky = Item("Rubber Duck", 10)
rubber_ducky.description = "Your enemies will squeak in fear."
ensuite.item = rubber_ducky

medicine = Item("Medicine", 10)
medicine.description = "Able to restore your number of lives back to 10."
kitchen.item = medicine

key = Item("a Skeleton Key", 10)
key.description = "A key to lock and unlock any door."

warhammer = Item("Warhammer", 100)
warhammer.description = "The strongest weapon of them all. Perhaps strong enough to break through the front door..."

poleaxe = Item("Poleaxe", 95)
poleaxe.description = "Don't even think about it, just run in the opposite direction."

dave = Master("Dave", "The zombie that will never stop hunting you.", poleaxe, 95)
dave.set_conversation("Prepare to be annihilated!")

casper = Enemy("Casper", "The zombie that never sleeps.", crossbow, 70)
casper.set_conversation("A human? I will destroy you!")

sheldon = Enemy("Sheldon", "The zombie that never rests.", club, 40)
sheldon.set_conversation("No one wants to cross the mighty Sheldon!")

josh = Friend("Josh", "A nice guy.", key)
josh.set_conversation("Hello!")

prisoner = Friend("The Prisoner", "He has spent so long in his cell that he has forgotten everything except how to use his magic crafting table.", "")
prisoner.set_conversation("If you give me a Cloak of Invisibility, a Skeleton Key and a block of cheese, I will give you a weapon unlike anything this world has ever seen.")

zombies = [dave, casper, sheldon, josh, prisoner]

throne.set_character(dave)
dave.set_room(throne)
kitchen.set_character(josh)
josh.set_room(kitchen)
study.set_character(casper)
casper.set_room(study)
throne.set_character(sheldon)
sheldon.set_room(throne)
dungeon.set_character(prisoner)
prisoner.set_room(dungeon)

castle = RPGInfo("Castle of Horrors")
castle.welcome()
RPGInfo.info()
print("")
current_room = entrance
alive = True
print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
print("There are " + str(Enemy.num_enemies) + " enemies to fight and " + str(Master.num_masters) + " Master to fight.")
print("Escape the castle!")
backpack = []
max_lives = 10
lives = max_lives
xp = 0
prisoner_first = True
warhammer_trade_first = True

north = r"^[Nn][Oo]?[Rr]?[Tt]?[Hh]?$"
south = r"^[Ss][Oo]?[Uu]?[Tt]?[Hh]?$"
east = r"^[Ee][Aa]?[Ss]?[Tt]?$"
west = r"^[Ww][Ee]?[Ss]?[Tt]?$"
discuss = r"^[Dd][Ii]?[Ss]?[Cc]?[Uu]?[Ss]?[Ss]?$"
hug = r"^[Hh][Uu]?[Gg]?$"
trade = r"^[Tt][Rr]?[Aa]?[Dd]?[Ee]?$"
fight = r"^[Ff][Ii]?[Gg]?[Hh]?[Tt]?$"
item = r"^[Ii][Tt]?[Ee]?[Mm]?$"
reveal = r"^[Rr][Ee]?[Vv]?[Ee]?[Aa]?[Ll]?$"
yes = r"^[Yy][Ee]?[Ss]?$"
no = r"^[Nn][Oo]?$"
lock = r"^[Ll][Oo]?[Cc]?[Kk]?$"
instruct = r"^[Ii][Nn]?[Ss]?[Tt]?[Rr]?[Uu]?[Cc]?[Tt]?$"
medi = r"^[Mm][Ee]?[Dd]?[Ii]?[Cc]?[Ii]?[Nn]?[Ee]?$"

first = True
move_zombies = False


while lives > 0:
    print("-------------------------------------------------------------")
    print("")
    print("Lives: " + str(lives))
    print("XP: " + str(xp))
    print("")
    current_room.get_details()     
    inhabitants = current_room.get_character()
    if len(inhabitants) != 0:
        for inhabitant in inhabitants:
            print("")
            inhabitant.describe()
            print("")
            if isinstance(inhabitant, Friend):
                inhabitant_stuff = inhabitant.return_trading_items
                if len(inhabitant_stuff) != 0 and inhabitant_stuff[0] != "":
                    print(inhabitant.name, "has these Items: ")
                    for thing in range(1, len(inhabitant_stuff) + 1):
                        print(str(thing) + ": " + inhabitant_stuff[thing - 1].name)
            else:
                fighting_stuff = inhabitant.weapon
                print(inhabitant.name + " will fight with a " + fighting_stuff.name + ".")
                print(fighting_stuff.description)
                    
    items = current_room.item
    if len(items) != 0:
        for i in items:
            i.describe()

    room_zombies = []
    for zombie in inhabitants:
        if isinstance(zombie, Enemy) or isinstance(zombie, Master):
            room_zombies.append(zombie)
    
    if len(room_zombies) > 0:
        room_zombies = sorted(room_zombies, key = lambda x:x.strength)
        zombie = room_zombies[-1]
        print("")
        print(zombie.name, "has challenged you to a fight!")
        input("Press enter to continue...")
        
        if len(backpack) != 0:
            print("The contents of your backpack are as follows...")
            for thing in range(1, len(backpack) + 1):
                print(str(thing) + ": " + backpack[thing - 1].name)
            fought = False
            while not fought:
                combat_item = (input("What would you like to fight with?")).lower()
                for choice in backpack:
                    if choice.name.lower() == combat_item:
                        lives_data = zombie.fight(choice, xp)
                        if lives_data[0]:
                            lives = lives - 1
                            print("You have", lives, "lives remaining.")
                        else:
                            xp = xp + 10
                            print(zombie.name, "now has", lives_data[1], "lives remaining.")
                            if lives_data[1] == 0:
                                print("You have killed " + zombie.name + "!")
                                print("You can now take " + zombie.name + "'s weapon: His mighty " + zombie.weapon.name + "!")
                                backpack.append(zombie.weapon)
                                current_room.character.remove(zombie)
                                zombies.remove(zombie)
                                del zombie
                                xp = xp + 10
                        fought = True
                        break
                else:
                    print("You do not have that Item in your backpack. Try again.")
        else:
            print("Your backpack is empty, you cannot fight " + zombie.name + "!")
            print("You lose a life.")
            lives = lives - 1
            print("You have", lives, "lives remaining.")
        moving_zombies(zombies)
        moving_zombies(zombies)
        input("Press enter to continue...")
        continue

    if current_room == entrance and warhammer in backpack:
        print("")
        input("Press enter to break through the front door with the Warhammer and escape!")
        break

    if first:
        instructions()
        first = False

    print("")  
    print("What do you want to do?")
    
    command = input("\n>>>")
    command = command.lower()

    if search(north, command):
        data = current_room.move("north")
        current_room = data[0]
        move_zombies = data[1]
    
    elif search(south, command):
        data = current_room.move("south")
        current_room = data[0]
        move_zombies = data[1]
    
    elif search(east, command):
        data = current_room.move("east")
        current_room = data[0]
        move_zombies = data[1]
    
    elif search(west, command):
        data = current_room.move("west")
        current_room = data[0]
        move_zombies = data[1]
    
    elif search(discuss, command):
        if len(inhabitants) != 0:
            check = True
            while check:
                choice = input("Who would you like to talk to?")
                for person in inhabitants:
                    if choice.lower() == person.name.lower():
                        person.talk()
                        xp = xp + 5
                        check = False
                        break
                else:
                    print("I'm not sure what you said there. Say that again...")
        else:
            print("No one here to talk to!")
    elif search(fight, command):
        if len(inhabitants) != 0:
            check = True
            while check:
                choice = input("Who would you like to fight?")
                for person in inhabitants:
                    if choice.lower() == person.name.lower():
                        inhabitant = person
                        check = False
                        break
                else:
                    print("I'm not sure what you said there. Say that again...")
            print("I'm a Friend! You cannot fight me!")
        else:
            print("No one here to fight!")
    elif search(hug, command):
        if len(inhabitants) != 0:
            check = True
            while check:
                choice = input("Who would you like to hug?")
                for person in inhabitants:
                    if choice.lower() == person.name.lower():
                        if isinstance(person, Friend):
                            person.hug()
                            xp = xp + 5
                        else:
                            print("Don't even think about it.")
                        check = False
                        break
                else:
                    print("I'm not sure what you said there. Say that again...")
        else:
            print("No one here to hug!")
    elif search(item, command):
        if len(items) != 0:
            found_item = False
            while not found_item:
                input_name = (input("Please type in the name of the item you want to pick up...\n>>>")).lower()
                for i in items:
                    if input_name == i.name.lower():
                        backpack.append(i)
                        print("The", i.name, "has been successfully added to your backpack.")
                        xp = xp + 5
                        items.remove(i)
                        current_room.item = items
                        found_item = True
                        break
                else:
                    print("Hmmm ... that doesn't seem to be in this room.")
                    continue
        else:
            print("No items here to take!")
    elif search(reveal, command):
        if len(backpack) != 0:
            print("The contents of your backpack are as follows...")
            for thing in range(1, len(backpack) + 1):
                print(str(thing) + ": " + backpack[thing - 1].name)
        else:
            print("Nothing in your backpack!")
    elif search(trade, command):
        if len(inhabitants) != 0:
            check = True
            while check:
                choice = input("Who would you like to trade with?")
                for person in inhabitants:
                    if choice.lower() == person.name.lower():
                        inhabitant = person
                        check = False
                        break
                else:
                    print("I'm not sure what you said there. Say that again...")
            if isinstance(inhabitant, Friend):
                print("To trade with " + inhabitant.name + ", you must give him 3 Items.")
                if len(backpack) >= 3:
                    giving = []
                    cancel = False
                    for i in range(3):
                        print("The current contents of your backpack are as follows...")
                        for thing in range(1, len(backpack) + 1):
                            print(str(thing) + ": " + backpack[thing - 1].name)
                        traded = False
                        while not traded:
                            print("What would you like to give to " + inhabitant.name + "?")
                            print("If you wish to cancel the trade, type 'X'.")
                            trade_item = (input(">>>")).lower()
                            if trade_item == "x":
                                print("You have cancelled the trade.")
                                for abc in giving:
                                    backpack.append(abc)
                                cancel = True
                                break
                            for choice in backpack:
                                if choice.name.lower() == trade_item:
                                    print("You give the " + trade_item + " to " + inhabitant.name + ".")
                                    print("")
                                    backpack.remove(choice)
                                    giving.append(choice)
                                    traded = True
                                    break
                            else:
                                print("You do not have that Item in your backpack. Try again.")
                        if cancel:
                            break
                    if not cancel:
                        if inhabitant == prisoner and sorted(giving, key = lambda x:x.name) == [cheese, cloak, key] and warhammer_trade_first:
                            warhammer_trade_first = False
                            prisoner.return_trading_items = [key, cloak, cheese]
                            backpack.append(warhammer)
                            print("The prisoner gave you a Warhammer!")
                            print(warhammer.description)
                            print("")
                                
                        else:
                            return_trade = inhabitant.trade(giving)
                            for i in return_trade:
                                if i != "":
                                    backpack.append(i)
                        xp = xp + 20
                    
                else:
                    print("You do not have enough Items to trade with " + inhabitant.name + "!")
            else:
                print("Trading? Pathetic! Fight me!")
        else:
            print("No one in the room to trade with!")
    elif search(lock, command):
        if key in backpack:
            while True:
                direction = input("In which direction do you want to lock / unlock a door?")
                if search(north, direction):
                    current_room.lock("north")
                    break
                elif search(south, direction):
                    current_room.lock("south")
                    break
                elif search(east, direction):
                    current_room.lock("east")
                    break
                elif search(west, direction):
                    current_room.lock("west")
                    break
                else:
                    print("I'm not sure what you said there. Say that again...")
        else:
            print("You cannot lock or unlock doors.")
    elif search(instruct, command):
        first = True

    elif search(medi, command):
        if medicine in backpack:
            input("Press enter to use your medicine...")
            print("")
            print("Your lives have been restored!")
            lives = max_lives
            backpack.remove(medicine)
        else:
            print("You do not have any medicine!")
    else:
        print("I'm not sure what you said there. Say that again...")
    input("Press Enter to continue...")
    if move_zombies:
        if ((barracks.linked_rooms)["south"])[1] and prisoner_first:
            prisoner_first = False
            zombies.remove(prisoner)
            moving_zombies(zombies)
            zombies.append(prisoner)
        else:
            moving_zombies(zombies)
        move_zombies = False

print("")
if lives > 0:
    print("Congratulations!")
    print("You win!")
else:
    print("Ha!")
    print("You lost!")

print("")
RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()
